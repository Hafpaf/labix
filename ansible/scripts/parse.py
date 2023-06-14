#!/usr/bin/python3

import yaml
from jinja2 import Environment, FileSystemLoader
from sys import argv

def main(client_file, template_dir, output_dir):
    with open(client_file, 'r') as f:
        clients = yaml.safe_load(f)['clients']
        for client in clients:
            client['ipv4'] = client['ip'][0]
            client['ipv6'] = client['ip'][1]
            speed_in_G = client['speed'] >= 1000
            formatted_speed = '%.12g' % (client["speed"]/1000
                    if speed_in_G
                    else client["speed"])
            unit = "G" if speed_in_G else "M"
            client['speed_string'] = f'{formatted_speed}{unit}'

    env = Environment(loader=FileSystemLoader(template_dir))
    template_names = env.list_templates()
    print(f'Found templates: {", ".join(template_names)}')
    for name in template_names:
        print(f'Processing {name}... ', end='')
        template = env.get_template(name)
        output = template.render(clients=clients)
        first_line = output[:output.find('\n')]
        output_file = first_line[1:].strip()
        output_path = output_dir + output_file
        with open(output_path, 'w') as f:
            f.write(output)
            print(f'Successfully wrote to {output_path}')

if __name__ == '__main__':
    if len(argv) != 4:
        print('Usage: parse.py <client file> <template dir> <output dir>')
        exit(1)
    main(*argv[1:])
