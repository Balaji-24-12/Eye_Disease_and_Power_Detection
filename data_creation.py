import pandas as pd
import numpy as np
import random

def generate_eye_power_dataset(n=500):
    rows = []

    for i in range(1, n+1):

        # Age: 10–70
        age = random.randint(10, 70)

        # Pupil diameter
        pupil = round(np.random.uniform(3.0, 6.0), 2)

        # Axial length (drives power) - medically *plausible*
        axial = round(np.random.uniform(20.0, 27.5), 2)

        # Corneal curvature
        k1 = round(np.random.uniform(41.5, 45.5), 2)
        k2 = round(np.random.uniform(42.0, 46.0), 2)

        # Generate power based on axial length
        if axial > 24.5:
            # Myopia
            sphere = round(np.random.uniform(-6.0, -0.50), 2)
        elif axial < 22.5:
            # Hyperopia
            sphere = round(np.random.uniform(+0.50, +4.00), 2)
        else:
            # Normal
            sphere = round(np.random.uniform(-0.25, +0.25), 2)

        # Astigmatism
        cylinder = round(np.random.uniform(-2.5, 0.0), 2)
        axis = random.randint(0, 180)

        rows.append([
            f"IMG_{i:03}",
            age,
            sphere,
            cylinder,
            axis,
            pupil,
            axial,
            k1,
            k2
        ])

    df = pd.DataFrame(rows, columns=[
        "ImageID",
        "Age",
        "Sphere",
        "Cylinder",
        "Axis",
        "PupilDiameter_mm",
        "AxialLength_mm",
        "CornealCurvature_K1",
        "CornealCurvature_K2"
    ])

    df.to_csv("eye_power_dataset_500.csv", index=False)
    print("\nDataset created successfully: eye_power_dataset_500.csv")
    print(df.head())

generate_eye_power_dataset()
