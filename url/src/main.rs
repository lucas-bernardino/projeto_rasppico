use std::process::Stdio;

use lettre::{
    message::header::ContentType, transport::smtp::authentication::Credentials, Message,
    SmtpTransport, Transport,
};
use tokio::io::{AsyncBufReadExt, BufReader};

#[tokio::main]
async fn main() {
    //Nesse arquivo:
    //TODO: Criar servidor no localhostrun.
    //TODO: Mandar URL pro email
    //TODO: Ficar dentro de um loop verificando se essa url ainda é valida
    //TODO: Caso não for, começa o loop tudo de novo.

    //Em outro arquivo (ou separar em outras funções)
    //TODO: Precisa atualizar o .env do backend, flask e frontend.
}

async fn start_server() -> Result<String, Box<dyn std::error::Error + 'static>> {
    let init_command = tokio::process::Command::new("ssh")
        .args(["-R", "80:localhost:3000", "ssh.localhost.run"])
        .stdout(Stdio::piped())
        .spawn();

    let stdout = init_command?.stdout.take();

    let mut reader = match stdout {
        Some(s) => BufReader::new(s).lines(),
        None => return Err("Could not get stdout".into()),
    };

    let mut url = String::new();

    while let Some(line) = reader.next_line().await.unwrap() {
        if line.contains("https") {
            let remove_trash = line.trim().replace(" ", "");
            let vec_url = remove_trash.split(",").collect::<Vec<_>>();
            url = vec_url.get(1).unwrap().to_string();
            break;
        }
    }

    Ok(url)
}

async fn send_email(url: &String) -> Result<(), Box<dyn std::error::Error + 'static>> {
    let email = Message::builder()
        .from("microfoneprojeto@gmail.com".parse()?)
        .to("microfoneprojeto@gmail.com".parse()?)
        .subject("API")
        .header(ContentType::TEXT_PLAIN)
        .body(url.clone())?;

    let password = std::env::var("GMAIL_PASSWORD")?.replace("_", " ");

    let creds = Credentials::new("microfoneprojeto@gmail.com".to_owned(), password.to_owned());

    let mailer = SmtpTransport::relay("smtp.gmail.com")
        .unwrap()
        .credentials(creds)
        .build();

    match mailer.send(&email) {
        Ok(_) => println!("Email sent successfully!"),
        Err(e) => panic!("Could not send email: {e:?}"),
    }

    Ok(())
}

async fn init_server_email() -> Result<String, Box<dyn std::error::Error + 'static>> {
    let url = match start_server().await {
        Ok(u) => u,
        Err(e) => {
            return Err(format!(
                "Could not send email due to an error in starting the server\nError: {}",
                e.to_string()
            )
            .into())
        }
    };

    send_email(&url).await.unwrap();
    Ok(url)
}
