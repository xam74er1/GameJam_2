class World:
    def __init__(self,frame,maxX,maxY,gravity):
        self.frame = frame
        self.maxX = maxX
        self.maxY = maxY
        self.gravity = gravity
        self.listBlock = []