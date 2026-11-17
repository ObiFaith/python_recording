def  reverse_stack(stack: list[int]):
    def swap(stack: list[int], left, right, count):
        if len(stack) <= 1:
            return stack

        stack[right], stack[left] = stack[left], stack[right]

        if count > 0:
            swap(stack, left+1, right-1, count-1)

    stack_len = len(stack)
    return swap(stack, 0, stack_len-1, stack_len // 2 - 1)

stack = [1, 2, 3, 4, 5, 6]
reverse_stack(stack)
print(stack)
