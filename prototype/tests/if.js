true.if = (trueBlock, falseBlock) => trueBlock()
true.ifTrue = trueBlock => trueBlock()
true.ifFalse = falseBlock => null
false.if = (trueBlock, falseBlock) => falseBlock()
false.ifTrue = trueBlock => null
false.ifFalse = falseBlock => falseBlock()
