from multiprocessing import Pool

class TournamentEvaluator(object):
    def __init__(self, num_workers, eval_function, rounds=3, looserbracket=None, timeout=None, maxtasksperchild=None):
        self.eval_function = eval_function
        self.timeout = timeout
        self.rounds = rounds
        self.looserbracket = looserbracket
        self.pool = Pool(processes=num_workers, maxtasksperchild=maxtasksperchild)

    def __del__(self):
        self.pool.close()
        self.pool.join()
        self.pool.terminate()

    #TODO: integration of tournament steps (other rounds, until there is a winner)
    def evaluate(self, genomes, config):
        jobs = []
        genomes_half = len(genomes)/2
        pool_1 = genomes[genomes_half:]
        pool_2 = genomes[:genomes_half]
        winners = []
        loosers = []

        for i in range(genomes_half):
            jobs.append(self.pool.apply_async(self.eval_function, (pool_1[i], pool_2[i], config)))

        for job, (genome_id1, genome_1), (genome_id2, genome_2) in zip(jobs, pool_1, pool_2):

            genome_1_fitness, genome_2_fitness = job.get(timeout=self.timeout)
            genome_1.fitness = genome_1.fitness + genome_1_fitness
            genome_2.fitness = genome_2.fitness + genome_2_fitness

            if(genome_1.fitness > genome_2.fitness):
                winners.append(genome_1)
                loosers.append(genome_2)
            else:
                winners.append(genome_2)
                loosers.append(genome_1)


