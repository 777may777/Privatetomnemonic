ENGLISH

### Software Description

This script is designed to convert cryptocurrency private keys to mnemonics using the BIP-39 standard. The script reads the private keys from a file named `private.txt`, converts each private key to a mnemonic, and writes the resulting mnemonics to a file named `mne.txt`. In addition, it shows a progress bar during the conversion process so that the user can see the progress.

### Script Structure

1. **Main Functions**:
   - `private_key_to_mnemonic`: Converts a private key in hexadecimal format to a BIP-39 mnemonic.
   - `read_private_keys`: Reads private keys from a file and returns them as a list.
   - `write_mnemonics`: Write the mnemonics to a file.
   - `main`: Controls the flow of the program, calling the read, convert and write functions, and displaying the progress bar.

2. **Bookstores**:
   - `bip_utils.Bip39MnemonicGenerator`: Used to generate BIP-39 mnemonics.
   - `binascii`: To convert private keys from hexadecimal to bytes.
   - `tqdm`: To show the progress bar.
2. **Bookstores**:
   - `bip_utils.Bip39MnemonicGenerator`: Used to generate BIP-39 mnemonics.
   - `binascii`: To convert private keys from hexadecimal to bytes.
   - `tqdm`: To show the progress bar.

### Execution Modes

The script is run from the command line, and requires no additional arguments. It must simply be located in the same directory as the `private.txt` file, or the correct path to the private key file must be specified.

### Execution Example

1. **Prepare the `private.txt` file**:
   - Create a file called `private.txt` in the same directory as the script. Each line of this file must contain a private key in hexadecimal format.

   ```plaintext
   4c3c2c2b2a292827262524232221201f1e1d1c1b1a191817161514131211100f
   5f6e7d8c9b0a0b1c2d3e4f5e6d7c8b9a8b7c6d5e4f3e2d1c0b1a2b3c4d5e6f7g
   ```

2. **Run the script**:
   - Open a terminal or command line.
   - Navigate to the directory where the script is located.
   - Run the script using Python:

   ```bash
   python script_name.py
   ```

   Replace `script_name.py` with the name of the script file.

### Complete Example

Below is a complete example of the process, `main.py`.

#### Contents of File `private.txt`

```plaintext
4c3c2c2b2a292827262524232221201f1e1d1c1b1a191817161514131211100f
5f6e7d8c9b0a0b1c2d3e4f5e6d7c8b9a8b7c6d5e4f3e2d1c0b1a2b3c4d5e6f7g
```

#### Script Execution

```bash
python main.py
```
#### Expected Output

The script will read the private keys from the `private.txt` file, convert each one to a BIP-39 mnemonic, and write the resulting mnemonics to a file called `mne.txt`. During the process, it will display a progress bar indicating the percentage of private keys converted.

### Contents of File `mne.txt`

After running the script, the `mne.txt` file will contain the corresponding mnemonics:

```plaintext
abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about
abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about
```

(Note: The actual mnemonics generated will depend on the private keys provided.)

This script simplifies the conversion of private keys to mnemonics and provides a friendly user interface with a progress bar that makes it easy to follow the process.



ESPAÑOL

### Descripción del Software

Este script está diseñado para convertir claves privadas de criptomonedas a mnemónicos utilizando el estándar BIP-39. El script lee las claves privadas desde un archivo llamado `private.txt`, convierte cada clave privada a un mnemónico y escribe los mnemónicos resultantes en un archivo llamado `mne.txt`. Además, muestra una barra de progreso durante el proceso de conversión para que el usuario pueda ver el avance.

### Estructura del Script

1. **Funciones Principales**:
   - `private_key_to_mnemonic`: Convierte una clave privada en formato hexadecimal a un mnemónico BIP-39.
   - `read_private_keys`: Lee las claves privadas desde un archivo y las retorna como una lista.
   - `write_mnemonics`: Escribe los mnemónicos en un archivo.
   - `main`: Controla el flujo del programa, llamando a las funciones de lectura, conversión y escritura, y mostrando la barra de progreso.

2. **Librerías**:
   - `bip_utils.Bip39MnemonicGenerator`: Utilizada para generar mnemónicos BIP-39.
   - `binascii`: Para convertir las claves privadas de hexadecimal a bytes.
   - `tqdm`: Para mostrar la barra de progreso.

### Modos de Ejecución

El script se ejecuta desde la línea de comandos, y no requiere argumentos adicionales. Simplemente debe estar ubicado en el mismo directorio que el archivo `private.txt`, o debe especificarse la ruta correcta para el archivo de claves privadas.

### Ejemplo de Ejecución

1. **Prepara el archivo `private.txt`**:
   - Crea un archivo llamado `private.txt` en el mismo directorio que el script. Cada línea de este archivo debe contener una clave privada en formato hexadecimal.

   ```plaintext
   4c3c2c2b2a292827262524232221201f1e1d1c1b1a191817161514131211100f
   5f6e7d8c9b0a0b1c2d3e4f5e6d7c8b9a8b7c6d5e4f3e2d1c0b1a2b3c4d5e6f7g
   ```

2. **Ejecuta el script**:
   - Abre una terminal o línea de comandos.
   - Navega hasta el directorio donde se encuentra el script.
   - Ejecuta el script utilizando Python:

   ```bash
   python nombre_del_script.py
   ```

   Reemplaza `nombre_del_script.py` con el nombre del archivo del script.

### Ejemplo Completo

A continuación, se presenta un ejemplo completo del proceso, `main.py`.

#### Contenido del Archivo `private.txt`

```plaintext
4c3c2c2b2a292827262524232221201f1e1d1c1b1a191817161514131211100f
5f6e7d8c9b0a0b1c2d3e4f5e6d7c8b9a8b7c6d5e4f3e2d1c0b1a2b3c4d5e6f7g
```

#### Ejecución del Script

```bash
python main.py
```

#### Salida Esperada

El script leerá las claves privadas del archivo `private.txt`, convertirá cada una en un mnemónico BIP-39 y escribirá los mnemónicos resultantes en un archivo llamado `mne.txt`. Durante el proceso, mostrará una barra de progreso que indicará el porcentaje de claves privadas convertidas.

### Contenido del Archivo `mne.txt`

Después de ejecutar el script, el archivo `mne.txt` contendrá los mnemónicos correspondientes:

```plaintext
abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about
abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about
```

(Nota: Los mnemónicos reales generados dependerán de las claves privadas proporcionadas).

Este script simplifica la conversión de claves privadas a mnemónicos y proporciona una interfaz de usuario amigable mediante una barra de progreso que facilita el seguimiento del proceso.
