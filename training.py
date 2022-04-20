
import multiprocessing
import os
import pickle

import TournamentEvaluator
import PiecesMoves
import neat
#import visualize

new_board = [[8, 4, 6, 10, 12, 6, 4, 8], [2, 2, 2, 2, 2, 2, 2, 2], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1], [7, 3, 5, 9, 11, 5, 3, 7]]

runs_per_net = 3
simulation_seconds = 60.0


# Use the NN network phenotype
def eval_genome(genome1, genome2, config):
    P1 = neat.nn.FeedForwardNetwork.create(genome1, config)
    P2 = neat.nn.FeedForwardNetwork.create(genome2, config)

    turn = PiecesMoves.WHITE

    fitnesses = []

    fitnessP1 = 0.
    fitnessP2 = 0.

    for runs in range(runs_per_net):
        simP1 = PiecesMoves.Game(new_board, PiecesMoves.WHITE)
        simP2 = PiecesMoves.Game(new_board, PiecesMoves.BLACK)
        
        while True:
            if(turn == PiecesMoves.WHITE):
                inputs, target, to_move = simP1.Actions_List
                if(inputs == None and simP1.Is_in_check()):
                    fitnessP1 = fitnessP1 - 10.
                    fitnessP2 = fitnessP2 + 10.
                    break
                if(simP1.Is_Draw()):
                    break
                action = net.activate(inputs)
                turn = PiecesMoves.BLACK
            if(turn == PiecesMoves.BLACK):
                inputs, target, to_move = simP2.Actions_List
                if(inputs == None and simP2.Is_in_check()):
                    fitnessP2 = fitnessP2 - 10.
                    fitnessP1 = fitnessP1 + 10.
                    break
                if(simP2.Is_Draw()):
                    break
                action = net.activate(inputs)
                turn = PiecesMoves.WHITE

            # Apply action
            simP1.Set_Board_State(action)
            simP2.Set_Board_State(action)

    # The genome's fitness
    return fitnessP1, fitnessP2

#Should not work properly
#def eval_genomes(genomes, config):
#    genome1_tab = []
#    genome2_tab = []
#    for genome_id1, genome1 in genomes:
#        for genome_id2, genome2 in genomes:
#            if(genome_id1 == genome_id2):
#                break
#            else:
#                genome1.fitness, genome2.fitness = eval_genome(genome1, genome2, config)
#                genome1_tab.append(genome1.fitness)
#                genome2_tab.append(genome2.fitness)
#    genome1.fitness = sum(genome1_tab)
#    genome2.fitness = sum(genome2_tab)


def run():
    # Load the config file, which is assumed to live in
    # the same directory as this script.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward')
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)

    pop = neat.Population(config)
    stats = neat.StatisticsReporter()
    pop.add_reporter(stats)
    pop.add_reporter(neat.StdOutReporter(True))

    loosers = []

    #Approche problematique pour un tournoi
    
    while(len(winners) > 1):
        pe = TournamentEvaluator.TournamentEvaluator(multiprocessing.cpu_count(), eval_genome)
        # TODO: Run usage will lead to error
        winner = pop.run(pe.evaluate)


    # Save the winner.
    with open('winner-feedforward', 'wb') as f:
        pickle.dump(winner, f)

    print(winner)

    #visualize.plot_stats(stats, ylog=True, view=True, filename="feedforward-fitness.svg")
    #visualize.plot_species(stats, view=True, filename="feedforward-speciation.svg")
    #
    #node_names = {-1: 'x', -2: 'dx', -3: 'theta', -4: 'dtheta', 0: 'control'}
    #visualize.draw_net(config, winner, True, node_names=node_names)
    #
    #visualize.draw_net(config, winner, view=True, node_names=node_names,
    #                   filename="winner-feedforward.gv")
    #visualize.draw_net(config, winner, view=True, node_names=node_names,
    #                   filename="winner-feedforward-enabled-pruned.gv", prune_unused=True)


if __name__ == '__main__':
    run()