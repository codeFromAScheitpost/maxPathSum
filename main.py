import click


def max_sum(triangle: list[list[int]]):
    """
    Computes the max path sum for a triangle.

    :param triangle: list representation of a triangle with the list at triangle[0] has length 1 and for all i length(triangle[i])+1=length(triangle[i+1])
    :return: value of the max path sum
    """
    if len(triangle) < 1:
        raise ValueError("empty triangle input is not supported")
    # each iteration the triangle is shrunk by one line
    while len(triangle) != 1:

        last_line: list[int] = triangle.pop(len(triangle) - 1)
        second_to_last_line: list[int] = triangle.pop(len(triangle) - 1)
        for i in range(0, len(second_to_last_line)):
            second_to_last_line[i] += max(last_line[i], last_line[i + 1])
        triangle.append(second_to_last_line)

    return triangle[0][0]


def read_file_to_triangle(file_path: str):
    """
    Parses a file and turns it into a list representation of a triangle.

    :param file_path: the path of a file that represents a triangle. each line of the triangle is divided by \n each valule is seperated by a whitespace
    :return: the list representation of the triangle
    """
    with open(file_path, "r") as file:
        whole_file: str = file.read()
    lines = whole_file.splitlines()
    lines = list(map(lambda x: x.split(' '), lines))
    triangle: list[list[int]] = list(map(lambda x: list(map(lambda y: int(y), x)), lines))

    # checks if the input triangle is well-formed.
    for i in range(0, len(triangle) - 1):
        if len(triangle[i]) + 1 != len(triangle[i + 1]):
            raise ValueError("the input is malformed, not each line is followed by a line that is one element larger")

    return triangle


@click.command()
@click.option('-e', '--exercise', type=int, default=1)
def main(exercise: int):
    # to run part one use 1 as input, to run part two use 2.
    # the input was chosen because the exercise specified only those two problems a file input would be possible as well

    if exercise < 1 or exercise > 2:
        raise IndexError("input should be 1 or 2")

    exercise_files = ["ex01.txt", "triangle.txt"]
    read_triangle = read_file_to_triangle(exercise_files[exercise - 1])
    print("the length of the maximal path for part ", exercise, "is: ", max_sum(read_triangle))


if __name__ == '__main__':
    main()
