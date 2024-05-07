true.if = function (trueBlock, falseBlock) {
    return trueBlock()
}

true.ifTrue = function (trueBlock) {
    return trueBlock()
}
true.ifFalse = function (falseBlock) {
    return null
}


false.if = function (trueBlock, falseBlock) {
    return falseBlock()
}

false.ifTrue = function (trueBlock) {
    return null
}

false.ifFalse = function (falseBlock) {
    return null
}

// a = 5
// (0 < 5).if(() => "true".print(), () => "false".print() )
false.ifFalse.print()
Object.print()
