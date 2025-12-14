n = int(input())
c = 0
d = {
    "Tetrahedron" : 4,
    "Cube" : 6,
    "Octahedron" : 8,
    "Dodecahedron" : 12,
    "Icosahedron" : 20
}
for i in range(n):
    s = input()
    c = c + d[s]
print(c)