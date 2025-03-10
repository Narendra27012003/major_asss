import os
import subprocess

def run_command(command):
    """Run a shell command and print the output."""
    print(f"Running command: {command}")
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(result.stdout)

def create_angular_project():
    """Create a new Angular project."""
    project_name = "my-angular-app"
    run_command(f"ng new {project_name} --routing --style=scss")

def install_dependencies():
    """Install necessary dependencies for the Angular project."""
    project_name = "my-angular-app"
    os.chdir(project_name)
    run_command("ng add @ngrx/store")
    run_command("ng add @ngrx/effects")
    run_command("ng add @ngrx/store-devtools")
    run_command("ng add @angular/material")
    run_command("npm install rxjs")

def create_folder_structure():
    """Create a modular folder structure for the Angular project."""
    project_name = "my-angular-app"
    os.chdir(project_name)
    
    # Define the folder structure
    folder_structure = [
        "src/app/components/button",
        "src/app/components/modal",
        "src/app/components/form",
        "src/app/pages/home",
        "src/app/pages/dashboard",
        "src/app/pages/login",
        "src/app/pages/signup",
        "src/app/services",
        "src/app/state"
    ]
    
    # Create folders
    for folder in folder_structure:
        os.makedirs(folder, exist_ok=True)
    
    # Create index.ts files and component files without logic
    components = ["button", "modal", "form"]
    for component in components:
        with open(f"src/app/components/{component}/index.ts", "w") as f:
            f.write(f"export * from './{component}.component';\n")
        with open(f"src/app/components/{component}/{component}.component.ts", "w") as f:
            f.write(f"import {{ Component }} from '@angular/core';\n\n")
            f.write(f"@Component({{\n")
            f.write(f"  selector: 'app-{component}',\n")
            f.write(f"  templateUrl: './{component}.component.html',\n")
            f.write(f"  styleUrls: ['./{component}.component.scss']\n")
            f.write(f"}})\n")
            f.write(f"export class {component.capitalize()}Component {{}}\n")
    
    # Create page components without logic
    pages = ["home", "dashboard", "login", "signup"]
    for page in pages:
        with open(f"src/app/pages/{page}/{page}.component.ts", "w") as f:
            f.write(f"import {{ Component }} from '@angular/core';\n\n")
            f.write(f"@Component({{\n")
            f.write(f"  selector: 'app-{page}',\n")
            f.write(f"  templateUrl: './{page}.component.html',\n")
            f.write(f"  styleUrls: ['./{page}.component.scss']\n")
            f.write(f"}})\n")
            f.write(f"export class {page.capitalize()}Component {{}}\n")

    # Create services without logic
    services = ["api", "auth", "user"]
    for service in services:
        with open(f"src/app/services/{service}.service.ts", "w") as f:
            f.write(f"import {{ Injectable }} from '@angular/core';\n")
            f.write(f"import {{ HttpClient }} from '@angular/common/http';\n")
            f.write(f"import {{ Observable }} from 'rxjs';\n\n")
            f.write(f"@Injectable({{ providedIn: 'root' }})\n")
            f.write(f"export class {service.capitalize()}Service {{\n")
            f.write(f"  constructor(private http: HttpClient) {{}}\n")
            f.write(f"  // Define service methods here\n")
            f.write(f"}}\n")

    # Create state management files without logic
    with open("src/app/state/store.ts", "w") as f:
        f.write("// Store configuration goes here\n")
    
    with open("src/app/state/user.reducer.ts", "w") as f:
        f.write("// User reducer logic goes here\n")
    
    with open("src/app/state/settings.reducer.ts", "w") as f:
        f.write("// Settings reducer logic goes here\n")

def main():
    create_angular_project()
    install_dependencies()
    create_folder_structure()
    print("Angular project setup completed successfully.")

if __name__ == "__main__":
    main()
