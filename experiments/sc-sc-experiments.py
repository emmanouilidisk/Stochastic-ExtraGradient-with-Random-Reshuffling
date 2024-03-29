import optimizer_module as op
import numpy as np
import pickle

def experiment_sc_sc_RR_vs_SO_vsIG():
    # sc-sc problem SEG-RR vs SEG
    n = 100
    d = 1
    n_iter = 4 * 10 ** 6
    trials = 5
    mu = 1
    x0 = np.random.normal(0, 1, 2 * d)
    condition_num_list = [1, 5, 10]
    params_list = []  # list with the params of the experiments

    # # uncomment to run SEG vs SEG-RR
    # for i in range(len(condition_num_list)):
    #     print("started problem with condition_number:", condition_num_list[i])
    #     problem = op.problem(problem_type="quadratic", n=n, d=d, mu=mu, L=condition_num_list[i])
    #     optimizer = op.optimizer(problem)
    #
    #     gamma_1_max = problem.mu / (
    #             10 * (problem.L_max ** 2) * np.sqrt(10 * (problem.n ** 2) + 2 * problem.n + 54))
    #
    #     last_iterate_SEG, relative_error_SEG = optimizer.SEG(gamma_1=gamma_1_max,
    #                                                              gamma_2=2 * gamma_1_max, x0=x0,
    #                                                              n_iter=n_iter,
    #                                                              trials=trials, rr=False)
    #
    #     last_iterate_SEG_RR, relative_error_SEG_RR = optimizer.SEG(gamma_1=gamma_1_max,
    #                                                                   gamma_2=2 * gamma_1_max, x0=x0,
    #                                                                   n_iter=n_iter,
    #                                                                   trials=trials, rr=True)
    #     last_iterate_SO, relative_error_SO = optimizer.SEG(gamma_1=gamma_1_max, gamma_2=2 * gamma_1_max,
    #                                                               x0=x0,
    #                                                               n_iter=n_iter,
    #                                                               trials=trials, so=True)
    #
    #     last_iterate_IG, relative_error_IG = optimizer.SEG(gamma_1=gamma_1_max, gamma_2=2 * gamma_1_max,
    #                                                           x0=x0,
    #                                                           n_iter=n_iter,
    #                                                           trials=trials, ig=True)
    #
    #     # save results in file
    #     params = {"n": n,
    #               "dimension": d,
    #               "mu": mu,
    #               "condition_number": condition_num_list[i],
    #               "x0": x0,
    #               "stepsizes_used": {"gamma_1": gamma_1_max, "gamma_2": 2 * gamma_1_max},
    #               "relative_error_SEG": relative_error_SEG,
    #               "last_iterate_SEG": last_iterate_SEG,
    #               "relative_error_SEG_RR": relative_error_SEG_RR,
    #               "last_iterate_SEG_RR": last_iterate_SEG_RR,
    #               "relative_error_SO": relative_error_SO,
    #               "last_iterate_SO": last_iterate_SO,
    #               "relative_error_IG": relative_error_IG,
    #               "last_iterate_IG": last_iterate_IG,
    #               "iterations": n_iter,
    #               "trials": trials,
    #               "solution": problem.sol
    #               }
    #
    #     filename = "saved_checkpoints/sc_sc_RR_vs_SO_vs_IG_cond_num" + str(condition_num_list[i]) + ".pkl"
    #     with open(filename, 'wb') as f:
    #         pickle.dump(params, f)

    # create plots
    for i in range(len(condition_num_list)):
        # load results
        with open('saved_checkpoints/sc_sc_RR_vs_SO_vs_IG_cond_num' + str(condition_num_list[i]) + ".pkl", 'rb') as f:
            params_list = pickle.load(f)

        results_SEG_RR = params_list["relative_error_SEG_RR"]
        results_SEG = params_list["relative_error_SEG"]
        results_SO = params_list["relative_error_SO"]
        results_IG = params_list["relative_error_IG"]

        # sparsify results
        sparsified_results_SEG_RR = [results_SEG_RR[j] for j in range(len(results_SEG_RR)) if j % 10**5 == 0]
        sparsified_results_SEG = [results_SEG[j] for j in range(len(results_SEG)) if j % 10 ** 5 == 0]
        sparsified_results_SO = [results_SO[j] for j in range(len(results_SO)) if j % 10 ** 5 == 0]
        sparsified_results_IG = [results_IG[j] for j in range(len(results_IG)) if j % 10 ** 5 == 0]
        # plot results
        op.plot_multiple_var([sparsified_results_SEG, sparsified_results_SEG_RR, sparsified_results_SO, sparsified_results_IG], labels=["SEG", "SEG-RR", "SEG-SO", "IEG"], x_label="Iterations (x$10^5$)", y_label="Relative Error", title="SC-SC Problem ($\kappa=$"+str(condition_num_list[i])+")", save_figure=True, filename="SC_SC_RR_vs_SO_IG"+str(condition_num_list[i]))

def experiment_sc_sc_SEG_RR_vs_SEG_large_steps():
    # sc-sc problem SEG-RR vs SEG
    n = 100
    d = 100
    n_iter = 1 * 10 ** 5
    trials = 5
    mu = 1
    L_max = 1
    x0 = np.random.normal(0, 1, 2 * d)
    condition_num_list = [1, 5, 10]
    params_list = []  # list with the params of the experiments

    # # uncomment to run experiments
    # for i in range(len(condition_num_list)):
    #     condition_number = condition_num_list[i]
    #     problem = op.problem(problem_type="quadratic", n=n, d=d, mu=mu, L=condition_number)
    #     optimizer = op.optimizer(problem)
    #
    #     gamma1 = 1.0 / (6 * problem.L)
    #
    #     last_iterate_SEG_RR, relative_error_SEG_RR = optimizer.SEG(gamma_1=gamma1, gamma_2=4 * gamma1, x0=x0,
    #                                                                n_iter=n_iter,
    #                                                                trials=trials, rr=True)
    #     last_iterate_SEG, relative_error_SEG = optimizer.SEG(gamma_1=gamma1, gamma_2=4 * gamma1, x0=x0, n_iter=n_iter,
    #                                                          trials=trials, rr=False)
    #
    #     # save results in file
    #     params = {"n": n,
    #               "dimension": d,
    #               "mu": mu,
    #               "condition_number": condition_number,
    #               "x0": x0,
    #               "stepsizes_used": {"gamma_1": gamma1, "gamma_2": 4 * gamma1},
    #               "relative_error_SEG": relative_error_SEG,
    #               "last_iterate_SEG": last_iterate_SEG,
    #               "relative_error_SEG_RR": relative_error_SEG_RR,
    #               "last_iterate_SEG_RR": last_iterate_SEG_RR,
    #               "iterations": n_iter,
    #               "trials": trials
    #               }
    #     filename = "saved_checkpoints/sc_sc_SEG_vs_SEG_RR_large_steps_cond_num" + str(condition_num_list[i]) + ".pkl"
    #     with open(filename, 'wb') as f:
    #         pickle.dump(params, f)

    # # load results
    # create plots
    for i in range(len(condition_num_list)):
        with open('saved_checkpoints/sc_sc_SEG_vs_SEG_RR_large_steps_cond_num' + str(condition_num_list[i]) + '.pkl', 'rb') as f:
            params_list = pickle.load(f)

        condition_number = condition_num_list[i]
        results_SEG_RR = params_list["relative_error_SEG_RR"]
        results_SEG = params_list["relative_error_SEG"]
        # sparsify results
        sparsified_results_SEG_RR = [results_SEG_RR[i] for i in range(len(results_SEG_RR)) if i % 10**4 == 0]
        sparsified_results_SEG = [results_SEG[i] for i in range(len(results_SEG)) if i % 10 ** 4 == 0]
        # plot results
        op.plot_multiple_var([sparsified_results_SEG, sparsified_results_SEG_RR], labels=["SEG", "SEG-RR"], x_label="Iterations (x$10^4$)", y_label="Relative Error", title="SC-SC Problem ($\kappa=$"+str(condition_number)+")", save_figure=True, filename="Beyond_Strongly_Monotone_cond_num"+str(condition_number))

def experiment_2d_SEG_RR_vs_SEG_large_steps_further_experiments():
    # SEG-RR vs SEG experiment
    #
    n = 100
    d = 1
    n_iter = [1 * 10 ** 5, 1 * 10 ** 5, 10 ** 6]
    trials = 5
    x0 = np.random.normal(0, 1, 2 * d)
    condition_num_list = [1, 5, 10, 100]

    # # uncomment to run experiment
    # for i in range(len(condition_num_list)):
    #     # initialize problem
    #     condition_number = condition_num_list[i]
    #     print("start exp with condition_number ", condition_number)
    #     problem = op.problem(problem_type="quadratic", n=n, d=d, mu=1, L=condition_number)
    #     optimizer = op.optimizer(problem)
    #     # steps
    #     stepsize_list = [1.0 / (10 * problem.L_max), 1.0 / (100 * problem.L_max), 1.0 / (1000 * problem.L_max)]
    #     relative_error_SEG_RR_list = []
    #     relative_error_SEG_list = []
    #     final_point_SEG_RR_list = []
    #     final_point_SEG_list = []
    #
    #     for step in range(len(stepsize_list)):
    #         # Run SEG-RR
    #         final_point_SEG_RR, relative_error_SEG_RR = optimizer.SEG(gamma_1=stepsize_list[step], gamma_2=4 * stepsize_list[step],
    #                                                                  x0=x0,
    #                                                                  n_iter=n_iter[step],
    #                                                                  trials=trials,
    #                                                                  rr=True)
    #         # Run SEG
    #         final_point_SEG, relative_error_SEG = optimizer.SEG(gamma_1=stepsize_list[step],
    #                                                                 gamma_2=4 * stepsize_list[step], x0=x0,
    #                                                                 n_iter=n_iter[step], trials=trials,
    #                                                                 rr=False)
    #         relative_error_SEG_RR_list.append(relative_error_SEG_RR)
    #         relative_error_SEG_list.append(relative_error_SEG)
    #         final_point_SEG_RR_list.append(final_point_SEG_RR)
    #         final_point_SEG_list.append(final_point_SEG)
    #
    #     # save results
    #     results = {"n": n,
    #                "dimension": d,
    #                "lambda_min": 1,
    #                "condition_number": condition_num_list[i],
    #                "x0": x0,
    #                "stepsizes_used": stepsize_list,
    #                "relative_error_SEG_RR_list": relative_error_SEG_RR_list,
    #                "final_point_SEG_RR_list": final_point_SEG_RR_list,
    #                "relative_error_SEG_list": relative_error_SEG_list,
    #                "final_point_SEG_list": final_point_SEG_list,
    #                "solution": optimizer.problem.sol}
    #     with open('saved_checkpoints/sc_sc_SEG_RR_vs_SEG_large_steps_further_exp_cond_num' + str(
    #             condition_number) + '.pkl', 'wb') as f:
    #         pickle.dump(results, f)

    for i in range(len(condition_num_list)):
        condition_number = condition_num_list[i]
        # load results
        with open('saved_checkpoints/sc_sc_SEG_RR_vs_SEG_large_steps_further_exp_cond_num' + str(
                condition_number) + ".pkl", 'rb') as f:
            results = pickle.load(f)

        relative_error_SEG_RR_list = results["relative_error_SEG_RR_list"]
        relative_error_SEG_list = results["relative_error_SEG_list"]
        solution = results["solution"]
        # run for different steps
        for step in range(3):
            if step != 2:
                relative_error_SEG_RR = relative_error_SEG_RR_list[step]
                relative_error_SEG = relative_error_SEG_list[step]

                sparsified_relative_error_SEG_RR = [relative_error_SEG_RR[i] for i in range(len(relative_error_SEG_RR)) if
                                                    i % 10 ** 4 == 0]
                sparsified_relative_error_SEG = [relative_error_SEG[i] for i in range(len(relative_error_SEG)) if
                                                 i % 10 ** 4 == 0]

                op.plot_multiple_var([sparsified_relative_error_SEG, sparsified_relative_error_SEG_RR],
                                     labels=["SEG", "SEG-RR"],y_label="Relative Error",
                                     x_label="Iterations (x$10^4$)",
                                     title="SC-SC Problem ($L_{max}=$" + str(condition_number) + ", $\gamma_1 = 1/($"+str(10**(step+1))+"L))",
                                     save_figure=True, filename="SC_SC_further_exp_step_"+str(step) + "_cond_num_" + str(condition_number))
            else:
                relative_error_SEG_RR = relative_error_SEG_RR_list[step]
                relative_error_SEG = relative_error_SEG_list[step]

                sparsified_relative_error_SEG_RR = [relative_error_SEG_RR[i] for i in range(len(relative_error_SEG_RR))
                                                    if i % 10 ** 5 == 0]
                sparsified_relative_error_SEG = [relative_error_SEG[i] for i in range(len(relative_error_SEG)) if
                                                 i % 10 ** 5 == 0]

                op.plot_multiple_var([sparsified_relative_error_SEG, sparsified_relative_error_SEG_RR],
                                     labels=["SEG", "SEG-RR"], y_label="Relative Error",
                                     x_label="Iterations (x$10^5$)",
                                     title="SC-SC Problem ($L_{max}=$" + str(condition_number) + ", $\gamma_1 = 1/($"+str(10**(step+1))+"L))",
                                     save_figure=True,
                                     filename="SC_SC_further_exp_step_" + str(step) + "_cond_num_" + str(
                                         condition_number))

if __name__ == '__main__':
    print("Starting SC-SC experiments ...")
    print("Experiment 1 started ")
    experiment_sc_sc_RR_vs_SO_vsIG()

    print("Experiment 2 started ")
    experiment_sc_sc_SEG_RR_vs_SEG_large_steps()

    print("Experiment 3 started ")
    experiment_2d_SEG_RR_vs_SEG_large_steps_further_experiments()
