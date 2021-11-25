import latk

la = latk.Latk(init=True)

lines = []
with open("result.csv") as f:
    lines = f.readlines()

lineCounter = 0
points = []

for line in lines:
    if (line[0] != "#"):
        lineArr = line.split(",")
        try:
            index = int(lineArr[3])
            if (index == -1):
                continue
            elif (index == lineCounter):
                x = float(lineArr[0])
                y = float(lineArr[1])
                z = float(lineArr[2])
                points.append(latk.LatkPoint((x, y, z)))
            elif (index > lineCounter and len(points) > 0):
                stroke = latk.LatkStroke(points)
                la.layers[0].frames[0].strokes.append(stroke)
                points = []
                x = float(lineArr[0])
                y = float(lineArr[1])
                z = float(lineArr[2])
                points.append(latk.LatkPoint((x, y, z)))
        except:
            pass

la.write("result.latk")