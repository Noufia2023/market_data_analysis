def validate_sector(sector):
    allowed = ["pharmaceuticals", "technology", "agriculture"]
    return sector.lower() in allowed
