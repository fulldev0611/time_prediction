# developer: Taoshidev
# Copyright © 2023 Taoshi, LLC

class ValiMemoryCorruptDataException(Exception):
    def __init__(self, message):
        super().__init__(self, message)


class ValiBkpCorruptDataException(Exception):
    def __init__(self, message):
        super().__init__(self, message)