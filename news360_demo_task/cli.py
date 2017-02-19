import click

from news360_demo_task.simplifier import simplify


@click.command()
@click.help_option(
    help='Отобразить эту справочную информацию и завершить работу'
)
@click.option('-f', '--file', help='Файл с входными данными')
def main(file):
    """Тестовое задание для компании News360."""
    if file:
        read_file = file
        write_file = '{}.out'.format(read_file)
        with open(read_file, 'r') as input_file:
            with open(write_file, 'w') as output_file:
                for line in input_file:
                    try:
                        new_equation = simplify(line.strip())
                        output_file.write('{}\n'.format(new_equation))
                    except SyntaxError as error:
                        output_file.write('{}\n'.format(error))
        return
    while True:
        line = click.prompt('ndt > ', type=str)
        try:
            new_equation = simplify(line.strip())
            click.echo(new_equation)
        except SyntaxError as error:
            click.echo(str(error))
