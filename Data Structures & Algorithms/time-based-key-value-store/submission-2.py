class TimeMap:
  def __init__(self):
    self.hashmap = {}


  def set(self, key: str, value: str, timestamp: int) -> None:
    if key not in self.hashmap:
      self.hashmap[key] = [[value], [timestamp]]
    else:
      self.hashmap.get(key)[0].append(value)
      self.hashmap.get(key)[1].append(timestamp)
        

  def get(self, key: str, timestamp: int) -> str:
    if key not in self.hashmap:
      return ""
    values, times = self.hashmap.get(key)
    largest_prev = -1
    low = 0
    high = len(times) - 1
    while low <= high:
      mid = (high + low) // 2
      if times[mid] == timestamp:
        return values[mid]
      elif times[mid] < timestamp:
        low = mid + 1
      else:
        high = mid - 1
      if times[mid] > largest_prev and times[mid] <= timestamp:
        largest_prev = mid
    if largest_prev == -1:
      return ""
    return values[largest_prev]
