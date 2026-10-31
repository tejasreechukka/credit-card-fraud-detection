import numpy as np
from sklearn.model_selection import train_test_split

from config import RANDOM_STATE


def main():

    print("--- REPRODUCIBILITY CHECK ---")

    # Create sample transaction IDs
    transaction_ids = np.arange(1000)

    # Create sample target classes
    target = np.array([0] * 990 + [1] * 10)

    # First split
    train_1, test_1 = train_test_split(
        transaction_ids,
        test_size=0.20,
        random_state=RANDOM_STATE,
        stratify=target
    )

    # Second split with the same settings
    train_2, test_2 = train_test_split(
        transaction_ids,
        test_size=0.20,
        random_state=RANDOM_STATE,
        stratify=target
    )

    # Compare both results
    print("Training split identical:",
          np.array_equal(train_1, train_2))

    print("Testing split identical:",
          np.array_equal(test_1, test_2))

    print("Training records:", len(train_1))
    print("Testing records:", len(test_1))

    if np.array_equal(train_1, train_2) and np.array_equal(test_1, test_2):
        print("\nSUCCESS: Results are reproducible!")
    else:
        print("\nFAILED: Results are different!")


if __name__ == "__main__":
    main()