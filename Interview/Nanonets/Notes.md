## Interacting with files on remote sftp server through python script

- SFTP is a secure file transfer protocol used for transferring files over the internet. It helps you to file access, transfer and file management over any reliable data stream.

- Python provides a module called PySftp used to connect to the SFTP server. It is a simple interface to SFTP and uses SSH protocol version 2 implementations.

- pip install pysftp

### Access SFTP Server Using PySftp

    nano sftp.py
    import pysftp

    Hostname = "remote-ip-address"
    Username = "root"
    Password = "password"
    with pysftp.Connection(host=Hostname, username=Username, password=Password) as sftp:
    print("Connection successfully established ... ")
    # Switch to a remote directory
    sftp.cwd('/opt/')

    # Obtain structure of the remote directory '/opt'
    directory_structure = sftp.listdir_attr()

    # Print data
    for attr in directory_structure:
    print(attr.filename, attr)

### Upload a File to SFTP Using PySftp

- If you want to upload a file from your local system to the SFTP server using PySftp, you just need to use the sftp.put() method of the SFTP client.

        nano sftp.py
        import pysftp

        Hostname = "remote-ip-address"
        Username = "root"
        Password = "password"

        with pysftp.Connection(host=Hostname, username=Username, password=Password) as sftp:
        print("Connection successfully established ... ")

        # Define a file that you want to upload from your local directory
        localFilePath = '/boot/initrd.img'

        # Define the remote path where the file will be uploaded
        remoteFilePath = '/mnt/initrd.img'

        # Use put method to upload a file
        sftp.put(localFilePath, remoteFilePath)

        # Switch to a remote directory
        sftp.cwd('/mnt/')

        # Obtain structure of the remote directory '/opt'
        directory_structure = sftp.listdir_attr()

        # Print data
        for attr in directory_structure:
        print(attr.filename, attr)

<!-- https://www.ittsystems.com/how-to-access-sftp-server-in-python/#wbounce-modal -->


