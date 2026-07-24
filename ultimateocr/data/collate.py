
class OCRCollate:

    def __call__(self, batch):

        return {
            "samples": batch
        }
