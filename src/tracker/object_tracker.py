# src/tracker/object_tracker.py

import numpy as np

class ObjectTracker:
    """
    A simple centroid-based tracker that assigns unique IDs to detected objects
    and tracks them as they move across frames.
    """

    def __init__(self, max_lost=10):
        self.next_object_id = 0       # ID to assign to next new object
        self.objects = {}             # object_id -> centroid
        self.lost_counts = {}         # object_id -> frames lost
        self.max_lost = max_lost      # max frames allowed to be unseen

    def _compute_centroid(self, box):
        x1, y1, x2, y2 = box
        cx = int((x1 + x2) / 2)
        cy = int((y1 + y2) / 2)
        return (cx, cy)

    def update(self, detections):
        """
        Update tracker with new detections.
        detections format: [x1, y1, x2, y2, conf, cls]
        Returns list of tracked objects:
        [id, x1, y1, x2, y2, conf, cls]
        """

        if len(detections) == 0:
            # Increase lost count for all existing objects
            for object_id in list(self.lost_counts.keys()):
                self.lost_counts[object_id] += 1
                if self.lost_counts[object_id] > self.max_lost:
                    self._remove_object(object_id)
            return []

        new_centroids = np.array([
            self._compute_centroid(det[:4]) for det in detections
        ])

        object_ids = list(self.objects.keys())
        object_centroids = np.array(list(self.objects.values()))

        tracked_objects = []

        # Case 1: No existing objects — assign all new IDs
        if len(self.objects) == 0:
            for det, centroid in zip(detections, new_centroids):
                self._add_new_object(centroid)
                obj_id = self.next_object_id - 1
                tracked_objects.append([obj_id, *det])
            return tracked_objects

        # Compute distance matrix (existing objects vs new detections)
        distances = np.linalg.norm(
            object_centroids[:, np.newaxis] - new_centroids, axis=2
        )

        # Find best matches
        rows = distances.min(axis=1).argsort()
        cols = distances.argmin(axis=1)[rows]

        matched_new = set()
        matched_old = set()

        for row, col in zip(rows, cols):
            if row in matched_old or col in matched_new:
                continue

            object_id = object_ids[row]
            self.objects[object_id] = new_centroids[col]
            self.lost_counts[object_id] = 0  # reset lost count

            tracked_objects.append([object_id, *detections[col]])

            matched_old.add(row)
            matched_new.add(col)

        # Add new objects that didn't match with existing ones
        for i, det in enumerate(detections):
            if i not in matched_new:
                centroid = new_centroids[i]
                self._add_new_object(centroid)
                obj_id = self.next_object_id - 1
                tracked_objects.append([obj_id, *det])

        # Increase lost count for unmatched old objects
        for i, object_id in enumerate(object_ids):
            if i not in matched_old:
                self.lost_counts[object_id] += 1
                if self.lost_counts[object_id] > self.max_lost:
                    self._remove_object(object_id)

        return tracked_objects


    def _add_new_object(self, centroid):
        object_id = self.next_object_id
        self.objects[object_id] = centroid
        self.lost_counts[object_id] = 0
        self.next_object_id += 1

    def _remove_object(self, object_id):
        del self.objects[object_id]
        del self.lost_counts[object_id]
