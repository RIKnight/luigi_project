import luigi

class WorldTask(luigi.Task):
    world_file_name = luigi.Parameter(default='interim/world.txt')

    def run(self):
        with open(self.world_file_name, 'w') as world_file:
            world_file.write('World')
            world_file.close()

    def output(self):
        return luigi.LocalTarget(self.world_file_name)

if __name__=='__main__':
    luigi.run()