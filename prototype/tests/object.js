a = {
    "b": 1,
    "c": {
        "d": [ 10, 11 ]
    },
    "e": function() {
        return 5
    }
}

print(a.b + a.c.d[1])
