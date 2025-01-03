import subprocess
import os

def run_command(command):
    """Ejecuta un comando en el shell y espera su finalización."""
    result = subprocess.run(command, shell=True, text=True)
    if result.returncode != 0:
        print(f"Error al ejecutar: {' '.join(command)}")
        exit(1)

def main():
    try:
        # Obtener el nombre de la carpeta actual
        current_folder = os.path.basename(os.getcwd())
        
        # Determinar el repositorio remoto configurado (origin)
        result = subprocess.run("git config --get remote.origin.url", shell=True, text=True, capture_output=True)
        remote_url = result.stdout.strip() if result.returncode == 0 else "desconocido"
        
        # Imprimir información del repositorio
        print(f"\033[34mRepositorio remoto configurado: \033[32m{remote_url}\033[0m")
        
        # git add .
        print(f"\033[34mAgregando cambios sobre la carpeta \033[33m{current_folder}\033[34m...\033[0m")
        run_command("git add .")
        
        # git commit --amend
        print(f"\033[34mAmendiendo último commit...\033[0m")
        run_command("git commit --amend --no-edit")
        
        # git push origin main --force
        print(f"\033[34mPushing cambios con fuerza a main en el repositorio \033[32m{remote_url}\033[34m...\033[0m")
        run_command("git push origin main --force")
        
        print(f"\033[34mOperación completada exitosamente.\033[0m")
    except Exception as e:
        print(f"\033[31mError durante el proceso: {e}\033[0m")

if __name__ == "__main__":
    main()
