#%%
from qm_saas import QOPVersion
from qm_saas import QmSaas, ClusterConfig
from qm import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig
import matplotlib.pyplot as plt
from configuration import config

client = QmSaas(email="maximilian.zanner@quantum-brilliance.com", password="gozh0iBRMx9k")

cluster_config = ClusterConfig()
controller = cluster_config.controller()
controller.mw_fems(1)
controller.lf_fems(2)

with program() as prog:
    with infinite_loop_():
        play("x180", "NV")
#%%
with client.simulator(QOPVersion("v3_3_0"), cluster_config) as instance:
    # Use the instance object to simulate QUA programs
    qmm = QuantumMachinesManager(host=instance.host,
                                 port=instance.port,
                                 connection_headers=instance.default_connection_headers)
    # Continue as usual with opening a quantum machine and simulation of a qua program

    job = qmm.simulate(config, prog, SimulationConfig(2000))
    fetched_data = False
    while fetched_data is False:
        try:
            samps = job.get_simulated_samples()
            fetched_data = True
        except:
            plt.pause(3)

samps.con1.plot()

plt.show(block=True)



# %%
