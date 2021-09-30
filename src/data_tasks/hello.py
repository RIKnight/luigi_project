import luigi

class HelloTask(luigi.Task):
    hello_file_name = luigi.Parameter(default='interim/hello.txt')

    def run(self):
        with open(self.hello_file_name, 'w') as hello_file:
            hello_file.write('Hello')
            hello_file.close()

    def output(self):
        return luigi.LocalTarget(self.hello_file_name)

if __name__=='__main__':
    luigi.run()