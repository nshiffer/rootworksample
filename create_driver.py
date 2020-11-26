class Driver:
  def __init__(self, name):
    self.name = name
    self.avgSpeed = 0
    self.totalDist = 0
    self.pastTrips = []
  
  def prettyPrintInfo(self):
    if self.totalDist > 1:
      distString = self.totalDist+" miles"
    elif self.totalDist == 1:
      distString = self.totalDist+" mile"
    else:
      #Distance is zero so only print distance
      print(self.name+": "+self.totalDist+" miles")
      return
    
    print(self.name+": "+distStringt+" @ "+self.avgSpeed+" mph")
    return
