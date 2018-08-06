import numpy as np
from scipy.stats import expon
import scr.SamplePathClasses as PathCls
import scr.StatisticalClasses as StatCls
import numpy
from numpy.random import choice
import DT as DTb
from scipy.stats import expon
from numpy.random import choice
import random as random


class Patient:
    # ##run more than one patient through tree to find costs and utilities
    # run a patient
    def __init__(self):
        self._rnd = np.random
        # counts
        self._count_OS_Access = 0
        self._count_OS_NoAccess = 0
        self._count_OS_A_Surgery = 0
        self._count_OS_A_noSurgery = 0
        self._count_OS_S_Die = 0
        self._count_OS_S_Survive = 0
        self._count_OS_S_S_Comp = 0
        self._count_OS_S_S_NoComp = 0
        self._count_OS_S_S_C_Major = 0
        self._count_OS_S_S_C_Minor = 0
        self._count_OS_S_S_C_Major_Die = 0
        self._count_OS_S_S_C_Major_Survive = 0
        self._count_OS_A_NoSurgery_Die = 0
        self._count_OS_A_NoSurgery_Survive = 0
        self._count_OS_Managua = 0
        self._count_OS_NA_Disease = 0
        self._count_OS_Disease_Die = 0
        self._count_OS_Disease_Survive = 0
        self._count_OS_Managua_Die = 0
        self._count_OS_Managua_Survive = 0
        self._count_OS_Managua_Comp = 0
        self._count_OS_Managua_NoComp = 0
        self._count_OS_M_S_C_Major = 0
        self._count_OS_M_S_C_Minor = 0
        self._count_OS_M_S_C_Major_Die = 0
        self._count_OS_M_S_C_Major_Survive = 0
        self._count_NoOS_Access = 0
        self._count_NoOS_NoAccess = 0
        self._count_NoOS_A_Surgery = 0
        self._count_NoOS_A_NoSurgery = 0
        self._count_NoOS_S_Die = 0
        self._count_NoOS_S_Survive = 0
        self._count_NoOS_S_S_comp = 0
        self._count_NoOS_S_S_NoComp = 0
        self._count_NoOS_S_S_C_Major = 0
        self._count_NoOS_S_S_C_Minor = 0
        self._count_NoOS_S_S_C_M_Die = 0
        self._count_NoOS_S_S_C_M_Survive = 0
        self._count_NoOS_NS_Die = 0
        self._count_NoOS_NS_Survive = 0
        self._count_NoOS_NA_Managua = 0
        self._count_NoOS_NA_Disease = 0
        self._count_NoOS_NA_M_Die = 0
        self._count_NoOS_NA_M_Survive = 0
        self._count_NoOS_NA_M_Comp = 0
        self._count_NoOS_NA_M_NoComp = 0
        self._count_NoOS_NA_M_Comp_Major = 0
        self._count_NoOS_NA_M_Comp_Minor = 0
        self._count_NoOS_NA_M_C_M_Die = 0
        self._count_NoOS_NA_M_C_M_Survive = 0
        self._count_NoOS_NA_D_Die = 0
        self._count_NoOS_NA_D_Survive = 0
        # count * cost/utility value
        self._S_OS_Access_C = 0
        self._S_OS_Access_U = 0
        self._S_OS_NoAccess_C = 0
        self._S_OS_NoAccess_U = 0
        self._S_OS_A_Surgery_C = 0
        self._S_OS_A_Surgery_U = 0
        self._S_OS_A_noSurgery_C = 0
        self._S_OS_A_noSurgery_U = 0
        self._S_OS_S_Die_C = 0
        self._S_OS_S_Die_U = 0
        self._S_OS_S_Survive_C = 0
        self._S_OS_S_Survive_U = 0
        self._S_OS_S_S_Comp_C = 0
        self._S_OS_S_S_Comp_U = 0
        self._S_OS_S_S_NoComp_C = 0
        self._S_OS_S_S_NoComp_U = 0
        self._S_OS_S_S_C_Major_C = 0
        self._S_OS_S_S_C_Major_U = 0
        self._S_OS_S_S_C_Minor_C = 0
        self._S_OS_S_S_C_Minor_U = 0
        self._S_OS_S_S_C_Major_Die_C = 0
        self._S_OS_S_S_C_Major_Die_U = 0
        self._S_OS_S_S_C_Major_Survive_C = 0
        self._S_OS_S_S_C_Major_Survive_U = 0
        self._S_OS_A_NoSurgery_Die_C = 0
        self._S_OS_A_NoSurgery_Die_U = 0
        self._S_OS_A_NoSurgery_Survive_C = 0
        self._S_OS_A_NoSurgery_Survive_U = 0
        self._S_OS_Managua_C = 0
        self._S_OS_Managua_U = 0
        self._S_OS_NA_Disease_C = 0
        self._S_OS_NA_Disease_U = 0
        self._S_OS_Disease_Die_C = 0
        self._S_OS_Disease_Die_U = 0
        self._S_OS_Disease_Survive_C = 0
        self._S_OS_Disease_Survive_U = 0
        self._S_OS_Managua_Die_C = 0
        self._S_OS_Managua_Die_U = 0
        self._S_OS_Managua_Survive_C = 0
        self._S_OS_Managua_Survive_U = 0
        self._S_OS_Managua_Comp_C = 0
        self._S_OS_Managua_Comp_U = 0
        self._S_OS_Managua_NoComp_C = 0
        self._S_OS_Managua_NoComp_U = 0
        self._S_OS_M_S_C_Major_C = 0
        self._S_OS_M_S_C_Major_U = 0
        self._S_OS_M_S_C_Minor_C = 0
        self._S_OS_M_S_C_Minor_U = 0
        self._S_OS_M_S_C_Major_Die_C = 0
        self._S_OS_M_S_C_Major_Die_U = 0
        self._S_OS_M_S_C_Major_Survive_C = 0
        self._S_OS_M_S_C_Major_survive_U = 0
        self._S_NoOS_Access_C = 0
        self._S_NoOS_Access_U = 0
        self._S_NoOS_NoAccess_C = 0
        self._S_NoOS_NoAccess_U = 0
        self._S_NoOS_A_Surgery_C = 0
        self._S_NoOS_A_Surgery_U = 0
        self._S_NoOS_A_NoSurgery_C = 0
        self._S_NoOS_A_NoSurgery_U = 0
        self._S_NoOS_S_Die_C = 0
        self._S_NoOS_S_Die_U = 0
        self._S_NoOS_S_Survive_C = 0
        self._S_NoOS_S_Survive_U = 0
        self._S_NoOS_S_S_comp_C = 0
        self._S_NoOS_S_S_comp_U = 0
        self._S_NoOS_S_S_NoComp_C = 0
        self._S_NoOS_S_S_NoComp_U = 0
        self._S_NoOS_S_S_C_Major_C = 0
        self._S_NoOS_S_S_C_Major_U = 0
        self._S_NoOS_S_S_C_Minor_C = 0
        self._S_NoOS_S_S_C_Minor_U = 0
        self._S_NoOS_S_S_C_M_Die_C = 0
        self._S_NoOS_S_S_C_M_Die_U = 0
        self._S_NoOS_S_S_C_M_Survive_C = 0
        self._S_NoOS_S_S_C_M_Survive_U = 0
        self._S_NoOS_NS_Die_C = 0
        self._S_NoOS_NS_Die_U =0
        self._S_NoOS_NS_Survive_C = 0
        self._S_NoOS_NS_Survive_U = 0
        self._S_NoOS_NA_Managua_C = 0
        self._S_NoOS_NA_Managua_U = 0
        self._S_NoOS_NA_Disease_C = 0
        self._S_NoOS_NA_Disease_U = 0
        self._S_NoOS_NA_M_Die_C = 0
        self._S_NoOS_NA_M_Die_U = 0
        self._S_NoOS_NA_M_Survive_C = 0
        self._S_NoOS_NA_M_Survive_U = 0
        self._S_NoOS_NA_M_Comp_C = 0
        self._S_NoOS_NA_M_Comp_U = 0
        self._S_NoOS_NA_M_NoComp_C = 0
        self._S_NoOS_NA_M_NoComp_U = 0
        self._S_NoOS_NA_M_Comp_Major_C = 0
        self._S_NoOS_NA_M_Comp_Major_U = 0
        self._S_NoOS_NA_M_Comp_Minor_C = 0
        self._S_NoOS_NA_M_Comp_Minor_U = 0
        self._S_NoOS_NA_M_C_M_Die_C = 0
        self._S_NoOS_NA_M_C_M_Die_U = 0
        self._S_NoOS_NA_M_C_M_Survive_C = 0
        self._S_NoOS_NA_M_C_M_Survive_U = 0
        self._S_NoOS_NA_Disease_Die_C = 0
        self._S_NoOS_NA_Disease_Die_U = 0
        self._S_NoOS_NA_D_Survive_C = 0
        self._S_NoOS_NA_D_Survive_U = 0

        self._total_OpSmile_costs = 0
        self._total_OpSmile_utilities = 0
        self._total_NoOpSmile_costs = 0
        self._total_NoOpSmile_utilities =0

        # dirichlet distribution:
        probs = np.random.dirichlet(alpha=(1, 2, 1), size=None)      # the numbers of alpha determine the
        # concentration of the probability for each option
        conditions_list = ['a', 'b', 'c']                               # list of conditions (refer to Conditions.py)

        self.draw = choice(a=conditions_list, p=probs)                  # drawing a random

    def simulate(self, n_of_patients):
        if self.draw == 'a':                # chooses tree/condition based off of Dirichlet distribution draw
            import DT_Condition_1 as D
        if self.draw == 'b':
            import DT_Condition_2 as D
        if self.draw == 'c':
            import DT_Condition_3 as D
        t = 0
        z = 0
        # OpSmile
        # randomizes patients into Access or No Access/ Managua
        for i in range(n_of_patients):
            if self._rnd.random_sample() < D.PR_OS_Access:
                self._count_OS_Access += 1  # count patients who go to access
            else:
                self._count_OS_NoAccess += 1  # count patients who go to no access
            t += 1

        # for those counts, you randomize them further
        # access -> surgery or no surgery
        for i in range(self._count_OS_Access):
            if self._rnd.random_sample() < D.PR_OS_A_Surgery:
                self._count_OS_A_Surgery += 1
            else:
                self._count_OS_A_noSurgery += 1

        # surgery -> survive or die
        for i in range(self._count_OS_A_Surgery):
            if self._rnd.random_sample() < D.PR_OS_S_Die:
                self._count_OS_S_Die += 1
            else:
                self._count_OS_S_Survive += 1

        # survive -> complications or no complications
        for i in range(self._count_OS_S_Survive):
            if self._rnd.random_sample() < D.PR_OS_S_S_Comp:
                self._count_OS_S_S_Comp += 1
            else:
                self._count_OS_S_S_NoComp += 1

        # complications -> major or minor comp
        for i in range (self._count_OS_S_S_Comp):
            if self._rnd.random_sample() < D.PR_OS_S_S_C_Major:
                self._count_OS_S_S_C_Major += 1
            else:
                self._count_OS_S_S_C_Minor += 1

        # major comp ->survive or die
        for i in range(self._count_OS_S_S_C_Major):
            if self._rnd.random_sample() <D.PR_OS_S_S_C_Major_Die:
                self._count_OS_S_S_C_Major_Die += 1
            else:
                self._count_OS_S_S_C_Major_Survive += 1

        # no surgery -> survive or die
        for i in range(self._count_OS_A_noSurgery):
            if self._rnd.random_sample() < D.PR_OS_A_NoSurgery_Die:
                self._count_OS_A_NoSurgery_Die += 1
            else:
                self._count_OS_A_NoSurgery_Survive += 1

        # no access -> Managua or Disease
        for i in range(self._count_OS_NoAccess):
            if self._rnd.random_sample() < D.PR_OS_Managua:
                self._count_OS_Managua += 1
            else:
                self._count_OS_NA_Disease += 1

        # Managua -> Survive or Die
        for i in range(self._count_OS_Managua):
            if self._rnd.random_sample() < D.PR_OS_Managua_Die:
                self._count_OS_Managua_Die += 1
            else:
                self._count_OS_Managua_Survive += 1

        # survive -> comp or no comp
        for i in range(self._count_OS_Managua_Survive):
            if self._rnd.random_sample() < D.PR_OS_M_S_Comp:
                self._count_OS_Managua_Comp += 1
            else:
                self._count_OS_Managua_NoComp += 1

        # comp -> major or minor comp
        for i in range(self._count_OS_Managua_Comp):
            if self._rnd.random_sample() < D.PR_OS_M_S_C_Major:
                self._count_OS_M_S_C_Major += 1
            else:
                self._count_OS_M_S_C_Minor += 1

        # Major comp -> survive or die
        for i in range(self._count_OS_M_S_C_Major):
            if self._rnd.random_sample() < D.PR_OS_M_S_C_Major_Die:
                self._count_OS_M_S_C_Major_Die += 1
            else:
                self._count_OS_M_S_C_Major_Survive += 1

        # Disease -> Survive or Die
        for i in range(self._count_OS_NA_Disease):
            if self._rnd.random_sample() < D.PR_OS_Disease_Die:
                self._count_OS_Disease_Die += 1
            else:
                self._count_OS_Disease_Survive += 1

        # NoOpSmile
        # Access or no access
        #while z < n_of_days:
        for i in range(n_of_patients):
            if self._rnd.random_sample() < D.PR_NoOS_Access:
                self._count_NoOS_Access += 1
            else:
                self._count_NoOS_NoAccess += 1
            z += 1

        # Access -> Surgery or no surgery
        for i in range(self._count_NoOS_Access):
            if self._rnd.random_sample() < D.PR_NoOS_A_Surgery:
                self._count_NoOS_A_Surgery += 1
            else:
                self._count_NoOS_A_NoSurgery += 1

        # surgery -> survive or die
        for i in range(self._count_NoOS_A_Surgery):
            if self._rnd.random_sample() < D.PR_NoOS_S_Die:
                self._count_NoOS_S_Die += 1
            else:
                self._count_NoOS_S_Survive += 1

        # survive -> comp or no comp
        for i in range(self._count_NoOS_S_Survive):
            if self._rnd.random_sample() < D.PR_NoOS_S_S_Comp:
                self._count_NoOS_S_S_comp += 1
            else:
                self._count_NoOS_S_S_NoComp += 1

        # comp -> minor or major
        for i in range(self._count_NoOS_S_S_comp):
            if self._rnd.random_sample() < D.PR_NoOS_S_S_C_Major:
                self._count_NoOS_S_S_C_Major += 1
            else:
                self._count_NoOS_S_S_C_Minor += 1

        # major -> survive or die
        for i in range(self._count_NoOS_S_S_C_Major):
            if self._rnd.random_sample() < D.PR_NoOS_S_S_C_M_Die:
                self._count_NoOS_S_S_C_M_Die += 1
            else:
                self._count_NoOS_S_S_C_M_Survive += 1

        # No surgery -> survive or die
        for i in range(self._count_NoOS_A_NoSurgery):
            if self._rnd.random_sample() < D.PR_NoOS_NS_Die:
                self._count_NoOS_NS_Die += 1
            else:
                self._count_NoOS_NS_Survive += 1

        # No access -> Managua or disease
        for i in range(self._count_NoOS_NoAccess):
            if self._rnd.random_sample() < D.PR_NoOS_NA_Managua:
                self._count_NoOS_NA_Managua += 1
            else:
                self._count_NoOS_NA_Disease += 1

        # Managua -> survive or die
        for i in range(self._count_NoOS_NA_Managua):
            if self._rnd.random_sample() < D.PR_NoOS_NA_M_Die:
                self._count_NoOS_NA_M_Die += 1
            else:
                self._count_NoOS_NA_M_Survive += 1

        # survive -> comp or no comp
        for i in range(self._count_NoOS_NA_M_Survive):
            if self._rnd.random_sample() < D.PR_NoOS_NA_M_Comp:
                self._count_NoOS_NA_M_Comp += 1
            else:
                self._count_NoOS_NA_M_NoComp += 1

        # comp -> major or minor
        for i in range(self._count_NoOS_NA_M_Comp):
            if self._rnd.random_sample() < D.PR_NoOS_NA_M_Comp_Major:
                self._count_NoOS_NA_M_Comp_Major += 1
            else:
                self._count_NoOS_NA_M_Comp_Minor += 1

        # major -> survive or die
        for i in range(self._count_NoOS_NA_M_Comp_Major):
            if self._rnd.random_sample() < D.PR_NoOS_NA_M_C_M_Die:
                self._count_NoOS_NA_M_C_M_Die += 1
            else:
                self._count_NoOS_NA_M_C_M_Survive += 1

        # disease -> survive or die
        for i in range(self._count_NoOS_NA_Disease):
            if self._rnd.random_sample() < D.PR_NoOS_NA_D_Die:
                self._count_NoOS_NA_D_Die += 1
            else:
                self._count_NoOS_NA_D_Survive += 1

        # multiply counts by cost and utilities and return total
        self._S_OS_A_Surgery_C = self._count_OS_A_Surgery * D.OS_A_Surgery_C
        self._S_OS_A_Surgery_U = self._count_OS_A_Surgery * D.OS_A_Surgery_U

        self._S_OS_A_noSurgery_C = self._count_OS_A_noSurgery * D.OS_A_NoSurgery_C
        self._S_OS_A_noSurgery_U = self._count_OS_A_noSurgery * D.OS_A_NoSurgery_U

        self._S_OS_NoAccess_U = self._count_OS_NoAccess * D.OS_NoAccess_U
        self._S_OS_NoAccess_C = self._count_OS_NoAccess * D.OS_NoAccess_C

        self._S_OS_Access_U = self._count_OS_Access * D.OS_Access_U
        self._S_OS_Access_C = self._count_OS_Access * D.OS_Access_C

        self._S_OS_S_Die_C = self._count_OS_S_Die * D.OS_S_Die_C
        self._S_OS_S_Die_U = self._count_OS_S_Die * D.OS_S_Die_U

        self._S_OS_S_Survive_C = self._count_OS_S_Survive * D.OS_A_S_Survive_C
        self._S_OS_S_Survive_U = self._count_OS_S_Survive * D.OS_A_S_Survive_U

        self._S_OS_S_Comp_C = self._count_OS_S_S_Comp * D.OS_A_S_S_Comp_C
        self._S_OS_S_Comp_U = self._count_OS_S_S_Comp * D.OS_A_S_S_Comp_U

        self._S_OS_S_S_NoComp_C = self._count_OS_S_S_NoComp * D.OS_S_S_NoComp_C
        self._S_OS_S_S_NoComp_U = self._count_OS_S_S_NoComp * D.OS_S_S_NoComp_U

        self._S_OS_S_S_C_Major_C = self._count_OS_S_S_C_Major * D.OS_A_S_S_C_Major_C
        self._S_OS_S_S_C_Major_U = self._count_OS_S_S_C_Major * D.OS_A_S_S_C_Major_U

        self._S_OS_S_S_C_Minor_C = self._count_OS_S_S_C_Minor * D.OS_S_S_Minor_C
        self._S_OS_S_S_C_Minor_U = self._count_OS_S_S_C_Minor * D.OS_S_S_Minor_U

        self._S_OS_S_S_C_Major_Die_C = self._count_OS_S_S_C_Major_Die * D.OS_S_S_C_Major_Die_C
        self._S_OS_S_S_C_Major_Die_U = self._count_OS_S_S_C_Major_Die * D.OS_S_S_C_Major_Die_U

        self._S_OS_S_S_C_Major_Survive_C = self._count_OS_S_S_C_Major_Survive * D.OS_S_S_C_Major_Survive_C
        self._S_OS_S_S_C_Major_Survive_U = self._count_OS_S_S_C_Major_Survive * D.OS_S_S_C_Major_Survive_U

        self._S_OS_A_NoSurgery_Die_C = self._count_OS_A_NoSurgery_Die * D.OS_NoSurgery_Die_C
        self._S_OS_A_NoSurgery_Die_U = self._count_OS_A_NoSurgery_Die * D.OS_NoSurgery_Die_U

        self._S_OS_A_NoSurgery_Survive_C = self._count_OS_A_NoSurgery_Survive * D.OS_NoSurgery_Survive_C
        self._S_OS_A_NoSurgery_Survive_U = self._count_OS_A_NoSurgery_Survive * D.OS_NoSurgery_Survive_U

        self._S_OS_Managua_C = self._count_OS_Managua * D.OS_NA_Managua_C
        self._S_OS_Managua_U = self._count_OS_Managua * D.OS_NA_Managua_U

        self._S_OS_NA_Disease_C = self._count_OS_NA_Disease * D.OS_NA_Disease_C
        self._S_OS_NA_Disease_U = self._count_OS_NA_Disease * D.OS_NA_Disease_U

        self._S_OS_Disease_Survive_C = self._count_OS_Disease_Survive * D.OS_Disease_Survive_C
        self._S_OS_Disease_Survive_U = self._count_OS_Disease_Survive * D.OS_Disease_Survive_U

        self._S_OS_Managua_Die_C = self._count_OS_Managua_Die * D.OS_Managua_Die_C
        self._S_OS_Managua_Die_U = self._count_OS_Managua_Die * D.OS_Managua_Die_U

        self._S_OS_Managua_Survive_C = self._count_OS_Managua_Survive * D.OS_NA_M_Survive_C
        self._S_OS_Managua_survive_U = self._count_OS_Managua_Survive * D.OS_NA_M_Survive_U

        self._S_OS_Managua_Comp_C = self._count_OS_Managua_Comp * D.OS_NA_M_S_Comp_C
        self._S_OS_Managua_Comp_U = self._count_OS_Managua_Comp * D.OS_NA_M_S_Comp_U

        self._S_OS_Managua_NoComp_C = self._count_OS_Managua_NoComp * D.OS_M_S_NoComp_C
        self._S_OS_Managua_NoComp_U = self._count_OS_Managua_NoComp * D.OS_M_S_NoComp_U

        self._S_OS_M_S_C_Major_C = self._count_OS_M_S_C_Major * D.OS_NA_M_S_C_Major_C
        self._S_OS_M_S_C_Major_U = self._count_OS_M_S_C_Major * D.OS_NA_M_S_C_Major_U

        self._S_OS_M_S_C_Minor_C = self._count_OS_M_S_C_Minor * D.OS_M_S_C_Minor_C
        self._S_OS_M_S_C_Minor_U = self._count_OS_M_S_C_Minor * D.OS_M_S_C_Minor_U

        self._S_OS_M_S_C_Major_Die_C = self._count_OS_M_S_C_Major_Die * D.OS_M_S_C_Major_Die_C
        self._S_OS_M_S_C_Major_Die_U = self._count_OS_M_S_C_Major_Die * D.OS_M_S_C_Major_Die_U

        self._S_OS_M_S_C_Major_Survive_C = self._count_OS_M_S_C_Major_Survive * D.OS_M_S_C_Major_Survive_C
        self._S_OS_M_S_C_Major_survive_U = self._count_OS_M_S_C_Major_Survive * D.OS_M_S_C_Major_Survive_U

        self._S_NoOS_Access_C = self._count_NoOS_Access * D.NoOS_Access_C
        self._S_NoOS_Access_U = self._count_NoOS_Access * D.NoOS_Access_U

        self._S_NoOS_NoAccess_C = self._count_NoOS_NoAccess * D.NoOS_NoAccess_C
        self._S_NoOS_NoAccess_U = self._count_NoOS_NoAccess * D.NoOS_NoAccess_U

        self._S_NoOS_A_Surgery_C = self._count_NoOS_A_Surgery * D.NoOS_A_Surgery_C
        self._S_NoOS_A_Surgery_U = self._count_NoOS_A_Surgery * D.NoOS_A_Surgery_U

        self._S_NoOS_NS_Survive_C = self._count_NoOS_NS_Survive * D.NoOS_NoSurgery_Survive_C
        self._S_NoOS_NS_Survive_U = self._count_NoOS_NS_Survive * D.NoOS_NoSurgery_Survive_U

        self._S_NoOS_A_NoSurgery_C = self._count_NoOS_A_NoSurgery * D.NoOS_A_NoSurgery_C
        self._S_NoOS_A_NoSurgery_U = self._count_NoOS_A_NoSurgery * D.NoOS_A_NoSurgery_U

        self._S_NoOS_S_Die_C = self._count_NoOS_S_Die * D.NoOS_S_Die_C
        self._S_NoOS_S_Die_U = self._count_NoOS_S_Die * D.NoOS_S_Die_U

        self._S_NoOS_S_Survive_C = self._count_NoOS_S_Survive * D.NoOS_A_S_Survive_C
        self._S_NoOS_S_Survive_U = self._count_NoOS_S_Survive * D.NoOS_A_S_Survive_U

        self._S_NoOS_S_S_comp_C = self._count_NoOS_S_S_comp * D.NoOS_A_S_S_Comp_C
        self._S_NoOS_S_S_comp_U = self._count_NoOS_S_S_comp * D.NoOS_A_S_S_Comp_U

        self._S_NoOS_S_S_NoComp_C = self._count_NoOS_S_S_NoComp * D.NoOS_S_S_NoComp_C
        self._S_NoOS_S_S_NoComp_U = self._count_NoOS_S_S_NoComp * D.NoOS_S_S_NoComp_U

        self._S_NoOS_S_S_C_Major_C = self._count_NoOS_S_S_C_Major * D.NoOS_A_S_S_C_Major_C
        self._S_NoOS_S_S_C_Major_U = self._count_NoOS_S_S_C_Major * D.NoOS_A_S_S_C_Major_U

        self._S_NoOS_S_S_C_Minor_C = self._count_NoOS_S_S_C_Minor * D.NoOS_S_S_Minor_C
        self._S_NoOS_S_S_C_Minor_U = self._count_NoOS_S_S_C_Minor * D.NoOS_S_S_Minor_U

        self._S_NoOS_S_S_C_M_Die_C = self._count_NoOS_S_S_C_M_Die * D.NoOS_S_S_C_Major_Die_C
        self._S_NoOS_S_S_C_M_Die_U = self._count_NoOS_S_S_C_M_Die * D.NoOS_S_S_C_Major_Die_U

        self._S_NoOS_S_S_C_M_Survive_C = self._count_NoOS_S_S_C_M_Survive * D.NoOS_S_S_C_Major_Survive_C
        self._S_NoOS_S_S_C_M_Survive_U = self._count_NoOS_S_S_C_M_Survive * D.NoOS_S_S_C_Major_Survive_U

        self._S_NoOS_NS_Die_C = self._count_NoOS_NS_Die * D.NoOS_NoSurgery_Die_C
        self._S_NoOS_NS_Die_U = self._count_NoOS_NS_Die * D.NoOS_NoSurgery_Die_U

        self._S_NoOS_NA_Survive_C = self._count_NoOS_NS_Survive * D.NoOS_NoSurgery_Survive_C
        self._S_NoOS_NA_Survive_U = self._count_NoOS_NS_Survive * D.NoOS_NoSurgery_Survive_U

        self._S_NoOS_NA_Managua_C = self._count_NoOS_NA_Managua * D.NoOS_NA_Managua_C
        self._S_NoOS_NA_Managua_U = self._count_NoOS_NA_Managua * D.NoOS_NA_Managua_U

        self._S_NoOS_NA_Disease_C = self._count_NoOS_NA_Disease * D.NoOS_NA_Disease_C
        self._S_NoOS_NA_Disease_U = self._count_NoOS_NA_Disease * D.NoOS_NA_Disease_U

        self._S_NoOS_NA_M_Die_C = self._count_NoOS_NA_M_Die * D.NoOS_Managua_Die_C
        self._S_NoOS_NA_M_Die_U = self._count_NoOS_NA_M_Die * D.NoOS_Managua_Die_U

        self._S_NoOS_NA_M_Survive_C = self._count_NoOS_NA_M_Survive * D.NoOS_NA_M_Survive_C
        self._S_NoOS_NA_M_Survive_U = self._count_NoOS_NA_M_Survive * D.NoOS_NA_M_Survive_U

        self._S_NoOS_NA_M_Comp_C = self._count_NoOS_NA_M_Comp * D.NoOS_NA_M_S_Comp_C
        self._S_NoOS_NA_M_Comp_U = self._count_NoOS_NA_M_Comp * D.NoOS_NA_M_S_Comp_U

        self._S_NoOS_NA_M_NoComp_C = self._count_NoOS_NA_M_NoComp * D.NoOS_M_S_NoComp_C
        self._S_NoOS_NA_M_NoComp_U = self._count_NoOS_NA_M_NoComp * D.NoOS_M_S_NoComp_U

        self._S_NoOS_NA_M_Comp_Major_C = self._count_NoOS_NA_M_Comp_Major * D.NoOS_NA_M_S_C_Major_C
        self._S_NoOS_NA_M_Comp_Major_U = self._count_NoOS_NA_M_Comp_Major * D.NoOS_NA_M_S_C_Major_U

        self._S_NoOS_NA_M_Comp_Minor_C = self._count_NoOS_NA_M_Comp_Minor * D.NoOS_M_S_C_Minor_C
        self._S_NoOS_NA_M_Comp_Minor_U = self._count_NoOS_NA_M_Comp_Minor * D.NoOS_M_S_C_Minor_U

        self._S_NoOS_NA_M_C_M_Die_C = self._count_NoOS_NA_M_C_M_Die * D.NoOS_M_S_C_Major_Die_C
        self._S_NoOS_NA_M_C_M_Die_U = self._count_NoOS_NA_M_C_M_Die * D.NoOS_M_S_C_Major_Die_U

        self._S_NoOS_NA_M_C_M_Survive_C = self._count_NoOS_NA_M_C_M_Survive * D.NoOS_M_S_C_Major_Survive_C
        self._S_NoOS_NA_M_C_M_Survive_U = self._count_NoOS_NA_M_C_M_Survive * D.NoOS_M_S_C_Major_Survive_U

        self._S_NoOS_NA_Disease_Die_C = self._count_NoOS_NA_D_Die * D.NoOS_Disease_Die_C
        self._S_NoOS_NA_Disease_Die_U = self._count_NoOS_NA_D_Die * D.NoOS_Disease_Die_U

        self._S_NoOS_NA_D_Survive_C = self._count_NoOS_NA_D_Survive * D.NoOS_Disease_Survive_C
        self._S_NoOS_NA_D_Survive_U = self._count_NoOS_NA_D_Survive * D.NoOS_Disease_Survive_U

        self._total_OpSmile_costs = self._S_OS_Access_C + self._S_OS_NoAccess_C + self._S_OS_A_Surgery_C + \
                                    self._S_OS_A_noSurgery_C + self._S_OS_S_Die_C + self._S_OS_S_Survive_C + \
                                    self._S_OS_S_Comp_C + self._S_OS_S_S_NoComp_C + self._S_OS_S_S_C_Major_C + \
                                    self._S_OS_S_S_C_Minor_C + self._S_OS_S_S_C_Major_Die_C + \
                                    self._S_OS_A_NoSurgery_Survive_C + self._S_OS_S_S_C_Major_Survive_C + \
                                    self._S_OS_A_NoSurgery_Die_C + self._S_OS_Managua_C + self._S_OS_NA_Disease_C + \
                                    self._S_OS_Managua_Die_C + self._S_OS_Managua_Survive_C + self._S_OS_Managua_Comp_C + \
                                    self._S_OS_Managua_NoComp_C + self._S_OS_M_S_C_Major_C + self._S_OS_M_S_C_Minor_C + \
                                    self._S_OS_M_S_C_Major_Die_C + self._S_OS_M_S_C_Major_Survive_C + \
                                    self._S_OS_Disease_Survive_C

        self._total_OpSmile_utilities = self._S_OS_Access_U + self._S_OS_NoAccess_U + self._S_OS_A_Surgery_U + \
                                        self._S_OS_A_noSurgery_U + self._S_OS_S_Die_U + self._S_OS_S_Survive_U + \
                                        self._S_OS_S_Comp_U + self._S_OS_S_S_NoComp_U + self._S_OS_S_S_C_Major_U + \
                                        self._S_OS_S_S_C_Minor_U + self._S_OS_S_S_C_Major_Die_U + \
                                        self._S_OS_A_NoSurgery_Die_U + self._S_OS_A_NoSurgery_Survive_U + \
                                        self._S_OS_Managua_U + self._S_OS_NA_Disease_U + self._S_OS_NA_Disease_U + \
                                        self._S_OS_Managua_Die_U + self._S_OS_Managua_survive_U + self._S_OS_Managua_Comp_U \
                                        + self._S_OS_Managua_NoComp_U + self._S_OS_M_S_C_Major_U + self._S_OS_M_S_C_Minor_U + \
                                        self._S_OS_M_S_C_Major_Die_U + self._S_OS_M_S_C_Major_survive_U + \
                                        self._S_OS_Disease_Survive_U + self._S_NoOS_NA_M_C_M_Survive_U + self._S_NoOS_NA_Disease_Die_U

        self._total_NoOpSmile_costs = self._S_NoOS_Access_C + self._S_NoOS_NoAccess_C + self._S_NoOS_A_Surgery_C + \
                                      self._S_NoOS_NS_Survive_C + self._S_NoOS_A_NoSurgery_C + self._S_NoOS_S_Die_C + \
                                      self._S_NoOS_S_Survive_C + self._S_NoOS_S_S_comp_C + self._S_NoOS_S_S_NoComp_C + \
                                      self._S_NoOS_S_S_C_Major_C + self._S_NoOS_S_S_C_Minor_C + \
                                      self._S_NoOS_S_S_C_M_Die_C + self._S_NoOS_S_S_C_M_Survive_C + self._S_NoOS_NS_Die_C \
                                      + self._S_NoOS_NA_Survive_C + self._S_NoOS_NA_Managua_C + self._S_NoOS_NA_Disease_C \
                                      + self._S_NoOS_NA_M_Die_C + self._S_NoOS_NA_M_Survive_C + self._S_NoOS_NA_M_Comp_C \
                                      + self._S_NoOS_NA_M_NoComp_C + self._S_NoOS_NA_M_Comp_Major_C + \
                                      self._S_NoOS_NA_M_Comp_Minor_C + self._S_NoOS_NA_M_C_M_Die_C + \
                                      self._S_NoOS_NA_M_C_M_Survive_C + self._S_NoOS_NA_Disease_Die_C + \
                                      self._S_NoOS_NA_D_Survive_C

        self._total_NoOpSmile_utilities = self._S_NoOS_Access_U + self._S_NoOS_NoAccess_U + self._S_NoOS_A_Surgery_U + \
                                          self._S_NoOS_NS_Survive_U + self._S_NoOS_A_NoSurgery_U + self._S_NoOS_S_Die_U \
                                          + self._S_NoOS_S_Survive_U + self._S_NoOS_S_S_comp_U + \
                                          self._S_NoOS_S_S_NoComp_U + self._S_NoOS_S_S_C_Major_U + \
                                          self._S_NoOS_S_S_C_Minor_U + self._S_NoOS_S_S_C_M_Die_U + \
                                          self._S_NoOS_S_S_C_M_Survive_U + self._S_NoOS_NS_Die_U + \
                                          self._S_NoOS_NA_Survive_U + self._S_NoOS_NA_Managua_U + \
                                          self._S_NoOS_NA_Disease_U + self._S_NoOS_NA_M_Die_U + \
                                          self._S_NoOS_NA_M_Survive_U + self._S_NoOS_NA_M_Comp_U + \
                                          self._S_NoOS_NA_M_NoComp_U + self._S_NoOS_NA_M_Comp_Major_U + \
                                          self._S_NoOS_NA_M_Comp_Minor_U + self._S_NoOS_NA_M_C_M_Die_U + \
                                          self._S_NoOS_NA_M_C_M_Survive_U + self._S_NoOS_NA_Disease_Die_U + \
                                          self._S_NoOS_NA_D_Survive_U

    def get_OS_cost(self):
        return self._total_OpSmile_costs

    def get_NoOS_cost(self):
        return self._total_NoOpSmile_costs

    def get_OS_utility(self):
        return self._total_OpSmile_utilities

    def get_NoOS_utility(self):
        return  self._total_NoOpSmile_utilities


class YearofPatients:
    def __init__(self, id):
        self._patients = []
        self._con_a_patients = []
        self._con_b_patients = []
        self._con_c_patients = []
        # eventually we'll want to add other metrics here. Like how many died, etc.

        self._initial_pop_size=100
        # fixed internally because we're going to make this number random eventually.
        # Maybe we'll change this later, but this should work for now.

        for i in range(self._initial_pop_size):
            patient = Patient()
            self._patients.append(patient)
            self.draw = patient.draw
            if self.draw == 'a':
                self._con_a_patients.append(patient)
            if self.draw == 'b':
                self._con_b_patients.append(patient)
            if self.draw == 'c':
                self._con_c_patients.append(patient)

    def simulate(self):
        """ simulate the cohort of patients over the specified number of time-steps
        :returns outputs from simulating this cohort
        """

        for patient in self._con_a_patients:
            patient.simulate(n_of_patients=len(self._con_a_patients))

        for patient in self._con_b_patients:
            patient.simulate(n_of_patients=len(self._con_b_patients))

        for patient in self._con_c_patients:
            patient.simulate(n_of_patients=len(self._con_c_patients))

        # return the cohort outputs
        return YearofPatientsOutputs(self)

    def get_number_of_patients(self):
        return self._initial_pop_size

    def get_patients(self):
        return self._patients

    def get_con_a_patients(self):
        return self._con_a_patients

    def get_con_b_patients(self):
        return self._con_b_patients

    def get_con_c_patients(self):
        return self._con_c_patients


class YearofPatientsOutputs:
    def __init__(self, simulated_cohort):
        """ extracts outputs from a simulated cohort
        :param simulated_cohort: a cohort after being simulated
        """

        self._OS_costs = []
        self._NoOS_costs = []
        self._OS_utilities = []
        self._NoOS_utilities = []

        self._con_a_patients_OS_costs = []
        self._con_a_patients_NoOS_costs = []
        self._con_a_patients_OS_utilities = []
        self._con_a_patients_NoOS_utilities = []

        self._con_b_patients_OS_costs = []
        self._con_b_patients_NoOS_costs = []
        self._con_b_patients_OS_utilities = []
        self._con_b_patients_NoOS_utilities = []

        self._con_c_patients_OS_costs = []
        self._con_c_patients_NoOS_costs = []
        self._con_c_patients_OS_utilities = []
        self._con_c_patients_NoOS_utilities = []

        for patient in simulated_cohort.get_patients():
            self._OS_costs.append(patient.get_OS_cost())
            self._NoOS_costs.append(patient.get_NoOS_cost())
            self._OS_utilities.append(patient.get_OS_utility())
            self._NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_a_patients():
            self._con_a_patients_OS_costs.append(patient.get_OS_cost())
            self._con_a_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_a_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_a_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_b_patients():
            self._con_b_patients_OS_costs.append(patient.get_OS_cost())
            self._con_b_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_b_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_b_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        for patient in simulated_cohort.get_con_c_patients():
            self._con_c_patients_OS_costs.append(patient.get_OS_cost())
            self._con_c_patients_NoOS_costs.append(patient.get_NoOS_cost())
            self._con_c_patients_OS_utilities.append(patient.get_OS_utility())
            self._con_c_patients_NoOS_utilities.append(patient.get_NoOS_utility())

        # summary statistics
        self._sumStat_OS_cost = StatCls.SummaryStat('Expected Op Smile Cost', self._OS_costs)
        self._sumStat_NoOS_cost = StatCls.SummaryStat('Expected No Op Smile Cost', self._NoOS_costs)
        self._sumStat_OS_utility = StatCls.SummaryStat('Expected Op Smile utility', self._OS_utilities)
        self._sumStat_NoOS_utility = StatCls.SummaryStat('Expected No Op Smile utility', self._NoOS_utilities)

        # summary Statistics condition A
        self._sumStat_con_a_OS_cost = StatCls.SummaryStat("Condition A Op Smile Cost", self._con_a_patients_OS_costs)
        self._sumStat_con_a_NoOS_cost = StatCls.SummaryStat("Condition A No Op Smile Cost", self._con_a_patients_NoOS_costs)
        self._sumStat_con_a_OS_utilities = StatCls.SummaryStat("Condition A Op Smile Utilities", self._con_a_patients_OS_utilities)
        self._sumStat_con_a_NoOS_utilities = StatCls.SummaryStat("Condition A No Op Smile Utilities", self._con_a_patients_NoOS_utilities)

        # summary statistics condition B
        self._sumStat_con_b_OS_cost = StatCls.SummaryStat("Condition B Op Smile Cost", self._con_b_patients_OS_costs)
        self._sumStat_con_b_NoOS_cost = StatCls.SummaryStat("Condition B No Op Smile Cost",
                                                            self._con_b_patients_NoOS_costs)
        self._sumStat_con_b_OS_utilities = StatCls.SummaryStat("Condition B Op Smile Utilities",
                                                               self._con_b_patients_OS_utilities)
        self._sumStat_con_b_NoOS_utilities = StatCls.SummaryStat("Condition B No Op Smile Utilities",
                                                                 self._con_b_patients_NoOS_utilities)

        # summary statistics condition C
        self._sumStat_con_c_OS_cost = StatCls.SummaryStat("Condition C Op Smile Cost", self._con_c_patients_OS_costs)
        self._sumStat_con_c_NoOS_cost = StatCls.SummaryStat("Condition C No Op Smile Cost",
                                                            self._con_c_patients_NoOS_costs)
        self._sumStat_con_c_OS_utilities = StatCls.SummaryStat("Condition C Op Smile Utilities",
                                                               self._con_c_patients_OS_utilities)
        self._sumStat_con_c_NoOS_utilities = StatCls.SummaryStat("Condition C No Op Smile Utilities",
                                                                 self._con_c_patients_NoOS_utilities)

    def get_con_a_OS_utilities(self):
        return self._con_a_patients_OS_utilities

    def get_con_a_NoOS_utilities(self):
        return self._con_a_patients_NoOS_utilities

    def get_OS_costs(self):
        return self._OS_costs

    def get_NoOS_costs(self):
        return self._NoOS_costs

    def get_OS_utilities(self):
        return self._OS_utilities

    def get_NoOS_utilities(self):
        return self._NoOS_utilities

    def get_sumStat_OS_cost(self):
        return self._sumStat_OS_cost

    def get_sumStat_NoOS_cost(self):
        return self._sumStat_NoOS_cost

    def get_sumStat_OS_utility(self):
        return self._sumStat_OS_utility

    def get_sumStat_NoOS_utility(self):
        return self._sumStat_NoOS_utility

# condition A
    def get_sumStat_con_a_OS_cost(self):
        return self._sumStat_con_a_OS_cost

    def get_sumStat_con_a_NoOS_cost(self):
        return self._sumStat_con_a_NoOS_cost

    def get_sumStat_con_a_OS_utilities(self):
        return self._sumStat_con_a_OS_utilities

    def get_sumStat_con_a_NoOS_utilities(self):
        return self._sumStat_con_a_NoOS_utilities

# condition B
    def get_sumStat_con_b_OS_cost(self):
        return self._sumStat_con_b_OS_cost

    def get_sumStat_con_b_NoOS_cost(self):
        return self._sumStat_con_b_NoOS_cost

    def get_sumStat_con_b_OS_utilities(self):
        return self._sumStat_con_b_OS_utilities

    def get_sumStat_con_b_NoOS_utilities(self):
        return self._sumStat_con_b_NoOS_utilities

# condition C
    def get_sumStat_con_c_OS_cost(self):
        return self._sumStat_con_c_OS_cost

    def get_sumStat_con_c_NoOS_cost(self):
        return self._sumStat_con_c_NoOS_cost

    def get_sumStat_con_c_OS_utilities(self):
        return self._sumStat_con_c_OS_utilities

    def get_sumStat_con_c_NoOS_utilities(self):

        return self._sumStat_con_c_NoOS_utilities
