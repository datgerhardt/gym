package main

type Compiler struct {
	code       string
	codeLength int
	position   int

	instructions []*Instruction
}

func NewCompiler(code string) *Compiler {
	return &Compiler{
		code:         code,
		codeLength:   len(code),
		instructions: []*Instruction{},
	}
}

func (c *Compiler) Compile() []*Instruction {
	loopStack := []int{}
	for c.position < c.codeLength {
		current := c.code[c.position]

		switch current {
		case '[':
			insPos := c.EmitWithArg(JumpIfZero, 0)
			loopStack = append(loopStack, insPos)
		case ']':
			openInstruction := loopStack[len(loopStack)-1]
			loopStack = loopStack[:len(loopStack)-1]
			closeInstruction := c.EmitWithArg(JumpIfNotZero, openInstruction)
			c.instructions[openInstruction].Argument = closeInstruction
		case '+':
			c.CompileFoldableInstruction('+', Plus)
		case '-':
			c.CompileFoldableInstruction('-', Minus)
		case '>':
			c.CompileFoldableInstruction('>', Right)
		case '<':
			c.CompileFoldableInstruction('<', Left)
		case '.':
			c.CompileFoldableInstruction('.', PutChar)
		case ',':
			c.CompileFoldableInstruction(',', ReadChar)
		}

		c.position++
	}

	return c.instructions
}

func (c *Compiler) CompileFoldableInstruction(char byte, insType InsType) {
	count := 1

	for c.position < c.codeLength-1 && c.code[c.position+1] == char {
		count++
		c.position++
	}
	c.EmitWithArg(insType, count)
}

func (c *Compiler) EmitWithArg(insType InsType, arg int) int {
	ins := &Instruction{Type: insType, Argument: arg}
	c.instructions = append(c.instructions, ins)
	return len(c.instructions) - 1
}
