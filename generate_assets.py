#!/usr/bin/env python3
"""
Asset Generator for LSNSES21SS13FEBAPS
Creates simulation GIFs, graphs, JSON outputs, quantum circuit diagrams,
and source code files in multiple languages.
"""
import os
import json
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def create_graphs():
    # Example graph: Yield improvement over time
    plt.figure(figsize=(8,6))
    years = np.arange(2025, 2031)
    yield_improvement = [5, 8, 12, 15, 18, 22]
    plt.plot(years, yield_improvement, marker='o')
    plt.title('Quantum-Enhanced Yield Improvement (%)')
    plt.xlabel('Year')
    plt.ylabel('Yield Improvement (%)')
    plt.grid(True)
    plt.savefig('assets/graphs/yield_improvement.png', dpi=150)
    plt.close()

def create_gif_simulations():
    # 2D simulation: moving sine wave (placeholder for quantum process)
    frames = []
    for i in range(20):
        plt.figure(figsize=(6,4))
        x = np.linspace(0, 4*np.pi, 200)
        y = np.sin(x + i*0.5)
        plt.plot(x, y, color='blue')
        plt.ylim(-1.5,1.5)
        plt.title('Quantum Oscillation (2D)')
        plt.savefig(f'/tmp/frame_{i:02d}.png', dpi=80)
        plt.close()
        frames.append(Image.open(f'/tmp/frame_{i:02d}.png'))
    frames[0].save('assets/simulations/quantum_2d.gif', save_all=True, append_images=frames[1:], duration=150, loop=0)
    # Cleanup
    for i in range(20):
        os.remove(f'/tmp/frame_{i:02d}.png')

def create_circuit_diagrams():
    # Placeholder quantum circuit diagram using qiskit (if available)
    try:
        from qiskit import QuantumCircuit
        qc = QuantumCircuit(4)
        qc.h(0)
        qc.cx(0,1)
        qc.cx(1,2)
        qc.cx(2,3)
        qc.measure_all()
        fig = qc.draw('mpl')
        fig.savefig('assets/circuits/vqe_circuit.png', dpi=150)
    except ImportError:
        # Fallback: create a simple text representation as image
        plt.figure(figsize=(10,2))
        plt.text(0.1,0.5,"H───●───●───●\n    │   │   │\n    0   1   2", fontsize=20)
        plt.axis('off')
        plt.savefig('assets/circuits/vqe_circuit.png', dpi=150, bbox_inches='tight')
        plt.close()

def create_json_outputs():
    # Example quantum simulation result
    data = {
        "reason": "exclusive_hardware_access",
        "qubit_hours": 20000,
        "speedup_factor": 8.5,
        "cost_savings_usd": 1500000,
        "partners": ["IBM Quantum", "IonQ", "Quantinuum"]
    }
    with open('assets/json/sample_result.json', 'w') as f:
        json.dump(data, f, indent=2)

def create_source_code_files():
    # Create 18+ language files with minimal quantum-related code
    languages = {
        "python": "qiskit_sim.py",
        "javascript": "quantum_calc.js",
        "java": "QuantumAnnealing.java",
        "cpp": "vqe_solver.cpp",
        "go": "grover_search.go",
        "rust": "lib.rs",
        "typescript": "qml.ts",
        "swift": "quantum.swift",
        "kotlin": "Qubit.kt",
        "r": "quantum_math.r",
        "matlab": "qc_simulation.m",
        "julia": "quantum_ops.jl",
        "csharp": "QSharpDriver.cs",
        "bash": "run_quantum.sh",
        "html": "quantum_dashboard.html",
        "react": "QuantumComponent.jsx",
        "next": "page.tsx",
        "vite": "main.js"
    }
    for lang, filename in languages.items():
        with open(f"assets/source_code/{filename}", 'w') as f:
            f.write(f"// {lang.upper()} example for quantum carbon intelligence\n")
            f.write("// Generated for LSNSES21SS13FEBAPS\n")
            if lang == "python":
                f.write("""
from qiskit import QuantumCircuit, Aer, execute
qc = QuantumCircuit(2,2)
qc.h(0)
qc.cx(0,1)
qc.measure([0,1],[0,1])
backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend, shots=1024)
result = job.result()
counts = result.get_counts(qc)
print(counts)
""")
            elif lang == "bash":
                f.write("#!/bin/bash\necho 'Submitting quantum job to IBM Q...'\n")
            else:
                f.write("\n// TODO: implement quantum algorithm for carbon capture\n")

if __name__ == "__main__":
    create_graphs()
    create_gif_simulations()
    create_circuit_diagrams()
    create_json_outputs()
    create_source_code_files()
    print("All assets generated.")
