# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    l = [x for x in range(1, 10)]

    for i in range(len(l) // 2):
        a = l[i]
        l[i] = l[len(l) - i - 1]
        l[len(l) - i - 1] = a
    print(l)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
