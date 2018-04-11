import cell
import settings

settings.init()
basemap = settings.UI_BASEMAP
road = basemap[1]

foo = [cell.Cell(x, y) for (x, y) in road]

print(foo[2].x, foo[2].y)