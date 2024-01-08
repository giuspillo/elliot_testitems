Implementation of [Elliot](https://elliot.readthedocs.io/en/latest/) in test rating mode

Modification have been applied to the files `elliot/elliot/dataset/dataset.py` and `elliot/elliot/dataset/modular_loaders/loader_coordinator_mixin.py`, in order to push the system generating prediction scores only for the items in the test set (these items must be associated to a positive rating).
Please follow the [original Elliot documentation](https://elliot.readthedocs.io/en/latest/) to train the recommendation models.
