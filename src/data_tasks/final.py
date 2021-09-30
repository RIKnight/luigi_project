import luigi

from hello import HelloTask
from world import WorldTask

class FinalTask(luigi.Task):
    # global variables
    hello_file_name = 'interim/hello.txt'
    world_file_name = 'interim/world.txt'
    hello_world_file_name =  'processed/hello_world.txt'

    def requires(self):
        yield HelloTask(self.hello_file_name)
        yield WorldTask(self.world_file_name)

    def output(self):
        return luigi.LocalTarget(self.hello_world_file_name)

    def run(self):
        with open(self.hello_file_name) as f:
            hello_lines = f.readlines()
        with open(self.world_file_name) as f:
            world_lines = f.readlines()
        with open(self.hello_world_file_name, 'w') as f:
            f.write(hello_lines[0]+' '+world_lines[0])
            f.close()
        

