from multiprocessing import Pool


class ParallelEvaluator(object):
    def __init__(self, num_workers, eval_function, timeout=None, maxtasksperchild=None):
        """
        eval_function should take one argument, a tuple of (genome object, config object),
        and return a single float (the genome's fitness).
        """
        self.eval_function = eval_function
        self.timeout = timeout
        self.pool = Pool(processes=num_workers, maxtasksperchild=maxtasksperchild)

    def __del__(self):
        self.pool.close()
        self.pool.join()
        self.pool.terminate()

    def evaluate(self, genomes, config):
        jobs = []
        for genome_id1, genome1 in genomes:
            for genome_id2, genome2 in genomes:
                if(genome_id1 == genome_id2):
                    break
                else:
                    jobs.append(self.pool.apply_async(self.eval_function, (genome1, genome2, config)))

        # assign the fitness back to each genome
        # This should not work properly
        for job, (genome_id1, genome_id2, genome) in zip(jobs, genomes):
            genome1.fitness, genome2.fitness = job.get(timeout=self.timeout)
