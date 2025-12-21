# src/counter/object_counter.py

class ObjectCounter:
    """
    Keeps track of unique object IDs and increments count only when
    a new object appears in the frame.
    """

    def __init__(self):
        self.counted_ids = set()   # Stores IDs already counted
        self.total_count = 0       # Running total

    def update(self, tracked_objects):
        """
        tracked_objects format:
        [id, x1, y1, x2, y2, confidence, class_id]

        Returns the updated total count.
        """
        
        for obj in tracked_objects:
            obj_id = obj[0]   # first element is ID

            # If this ID is new → increment count
            if obj_id not in self.counted_ids:
                self.counted_ids.add(obj_id)
                self.total_count += 1

        return self.total_count
