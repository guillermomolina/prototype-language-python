True.if = function (trueBlock, falseBlock) {
    return trueBlock()
}

True.ifTrue = function (trueBlock) {
    return trueBlock()
}

True.ifFalse = function (falseBlock) {
    return null
}

False.if = function (trueBlock, falseBlock) {
    return falseBlock()
}

False.ifTrue = function (trueBlock) {
    return null
}

False.ifFalse = function (falseBlock) {
    return falseBlock()
}
