import subprocess

def run_command(command):
    """Ejecuta un comando en el shell y espera su finalización."""
    result = subprocess.run(command, shell=True, text=True)
    if result.returncode != 0:
        print(f"Error al ejecutar: {' '.join(command)}")
        exit(1)

def main():
    try:
        # git add .
        print("Agregando cambios...")
        run_command("git add .")
        
        # git commit --amend
        print("Amendiendo último commit...")
        run_command("git commit --amend --no-edit")
        
        # git push origin main --force
        print("Pushing cambios con fuerza a main...")
        run_command("git push origin main --force")
        
        print("Operación completada exitosamente.")
    except Exception as e:
        print(f"Error durante el proceso: {e}")

if __name__ == "__main__":
    main()

