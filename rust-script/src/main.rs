use core::panic;
use std::{fmt::Display, fs};

const BACKEND_ENV_PATH: &str = "../backend/.env";
const VITE_ENV_PATH: &str = "../frontend/vite-project/.env";

#[derive(Debug)]
struct Info {
    backend: String,
    frontend: String,
    flask: String,
}

impl Info {
    fn add_field(&mut self, field: &str, value: &str) {
        match field {
            "backend" => self.backend = value.to_string(),
            "frontend" => self.frontend = value.to_string(),
            "flask" => self.flask = value.to_string(),
            _ => {}
        }
    }
}

impl Display for Info {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(
            f,
            "FRONTEND ROUTE: {}\nBACKEND ROUTE: {}\nFLASK ROUTE: {}",
            self.frontend, self.backend, self.flask
        )
    }
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let response = reqwest::get("http://127.0.0.1:4040/api/tunnels")
        .await?
        .json::<serde_json::Value>()
        .await?;
    let tunn_array = response.get("tunnels").unwrap().as_array().unwrap();

    let info = fill_struct(&tunn_array)?;

    let mut read_env_backend = fs::read_to_string(BACKEND_ENV_PATH)?;
    let offset = read_env_backend.rfind('=').unwrap();
    read_env_backend.replace_range(offset.., format!("={val}", val = info.backend).as_str());
    fs::write(BACKEND_ENV_PATH, &read_env_backend)?;

    let string_on_vite_env = format!(
        "VITE_BACKEND_URL={}\nVITE_FLASK_URL={}",
        info.backend, info.flask
    );
    fs::write(VITE_ENV_PATH, &string_on_vite_env)?;

    println!("{info}");

    Ok(())
}

fn fill_struct(
    tunnels_array: &Vec<serde_json::value::Value>,
) -> Result<Info, Box<dyn std::error::Error>> {
    let mut info = Info {
        backend: String::new(),
        frontend: String::new(),
        flask: String::new(),
    };

    for tunnel in tunnels_array {
        let public_url = match tunnel
            .get("public_url")
            .expect("ERROR: json field does not have 'public_url' field")
        {
            serde_json::Value::String(val) => val,
            _ => "",
        };
        let name = match tunnel
            .get("name")
            .expect("ERROR: json field does not have 'name' field")
        {
            serde_json::Value::String(val) => val,
            _ => panic!("ERROR: could not get name within json"),
        };
        info.add_field(name, public_url);
    }

    Ok(info)
}
