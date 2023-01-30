import subprocess


class A11yReport:
    def __init__(self, json_dir, engine, output_dir):
        self.json_dir = json_dir
        self.engine = engine
        self.output_dir = output_dir

    def generate_html_report(self):
        command = f"a11y-report -j={self.json_dir} -e={self.engine} -o={self.output_dir}"
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, encoding="utf-8")
        return result.stdout, result.stderr
