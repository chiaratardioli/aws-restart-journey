# Data Protection Using Encryption

Cryptography is the process of converting information into a secure format to protect its confidentiality, integrity, and authenticity. A key component of cryptography is encryption, which transforms readable data (plaintext) into an unreadable format (ciphertext). Only authorized users with the correct key can decrypt the data back into its original form.

In this lab, I worked with AWS services to understand how encryption is implemented in practice. I used AWS Key Management Service (KMS) to create and manage encryption keys, configured an EC2 instance to use these keys, and applied encryption and decryption processes to text files using the AWS Encryption CLI.

## Task 1: Create an AWS KMS Key
In this task, I created a symmetric encryption key using AWS KMS. I accessed the KMS service from the AWS Management Console and selected the option to create a new key.

I configured the key with the alias *MyKMSKey* and added a description indicating its purpose for encrypting and decrypting data files. I assigned administrative and usage permissions to the provided IAM role (voclabs), ensuring proper access control.

After reviewing the configuration, I completed the key creation process and saved the key’s ARN: `arn:aws:kms:us-west-2:450871918797:key/882db9db-9f7d-4a92-b676-10a13cb4f7ea`.
The ARN was essential for later steps where the key was used in encryption and decryption commands.

![KMS Key Created](./images/SE-03-kms-key-created.png)

## Task 2: Configure the File Server Instance
In this task, I connected to the preconfigured EC2 instance (File Server) using AWS Systems Manager Session Manager.

Once connected, I configured AWS CLI credentials on the instance. Initially, I entered placeholder values, then replaced them with valid credentials 
obtained from the lab environment. I edited the `~/.aws/credentials` file using the `vi` editor and verified the configuration.

After setting up credentials, I installed the AWS Encryption CLI using `pip3` and updated the system path to ensure the CLI could be executed globally.

These steps enabled the EC2 instance to securely interact with AWS KMS and perform encryption operations.

```bash
sh-4.2$ cd ~
sh-4.2$ aws configure
AWS Access Key ID [None]: 1
AWS Secret Access Key [None]: 1
Default region name [None]: us-west-2
Default output format [None]:
sh-4.2$ vi ~/.aws/credentials

sh-4.2$ pip3 install aws-encryption-sdk-cli
Defaulting to user installation because normal site-packages is not writeable
Collecting aws-encryption-sdk-cli
  Downloading aws_encryption_sdk_cli-4.3.0-py2.py3-none-any.whl (44 kB)
     |████████████████████████████████| 44 kB 3.4 MB/s
Requirement already satisfied: setuptools in /usr/lib/python3.7/site-packages (from aws-encryption-sdk-cli) (49.1.3)
Collecting base64io>=1.0.1
  Downloading base64io-1.0.3-py2.py3-none-any.whl (17 kB)
Collecting attrs>=17.1.0
  Downloading attrs-24.2.0-py3-none-any.whl (63 kB)
     |████████████████████████████████| 63 kB 4.7 MB/s
Collecting aws-encryption-sdk~=3.1
  Downloading aws_encryption_sdk-3.3.1-py2.py3-none-any.whl (90 kB)
     |████████████████████████████████| 90 kB 23.3 MB/s
Collecting importlib-metadata; python_version < "3.8"
  Downloading importlib_metadata-6.7.0-py3-none-any.whl (22 kB)
Collecting boto3>=1.10.0
  Downloading boto3-1.33.13-py3-none-any.whl (139 kB)
     |████████████████████████████████| 139 kB 62.2 MB/s
Collecting cryptography>=3.4.6
  Downloading cryptography-45.0.7-cp37-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (4.4 MB)
     |████████████████████████████████| 4.4 MB 60.7 MB/s
Collecting wrapt>=1.10.11
  Downloading wrapt-1.16.0-cp37-cp37m-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (77 kB)
     |████████████████████████████████| 77 kB 11.9 MB/s
Collecting typing-extensions>=3.6.4; python_version < "3.8"
  Downloading typing_extensions-4.7.1-py3-none-any.whl (33 kB)
Collecting zipp>=0.5
  Downloading zipp-3.15.0-py3-none-any.whl (6.8 kB)
Collecting jmespath<2.0.0,>=0.7.1
  Downloading jmespath-1.0.1-py3-none-any.whl (20 kB)
Collecting s3transfer<0.9.0,>=0.8.2
  Downloading s3transfer-0.8.2-py3-none-any.whl (82 kB)
     |████████████████████████████████| 82 kB 347 kB/s
Collecting botocore<1.34.0,>=1.33.13
  Downloading botocore-1.33.13-py3-none-any.whl (11.8 MB)
     |████████████████████████████████| 11.8 MB 37.9 MB/s
Collecting cffi>=1.14; platform_python_implementation != "PyPy"
  Downloading cffi-1.15.1-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (427 kB)
     |████████████████████████████████| 427 kB 50.6 MB/s
Collecting urllib3<1.27,>=1.25.4; python_version < "3.10"
  Downloading urllib3-1.26.20-py2.py3-none-any.whl (144 kB)
     |████████████████████████████████| 144 kB 73.5 MB/s
Collecting python-dateutil<3.0.0,>=2.1
  Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
     |████████████████████████████████| 229 kB 59.5 MB/s
Collecting pycparser
  Downloading pycparser-2.21-py2.py3-none-any.whl (118 kB)
     |████████████████████████████████| 118 kB 36.5 MB/s
Collecting six>=1.5
  Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: base64io, typing-extensions, zipp, importlib-metadata, attrs, jmespath, urllib3, six, python-dateutil, botocore, s3transfer, boto3, pycparser, cffi, cryptography, wrapt, aws-encryption-sdk, aws-encryption-sdk-cli
  WARNING: The script aws-encryption-cli is installed in '/home/ssm-user/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed attrs-24.2.0 aws-encryption-sdk-3.3.1 aws-encryption-sdk-cli-4.3.0 base64io-1.0.3 boto3-1.33.13 botocore-1.33.13 cffi-1.15.1 cryptography-45.0.7 importlib-metadata-6.7.0 jmespath-1.0.1 pycparser-2.21 python-dateutil-2.9.0.post0 s3transfer-0.8.2 six-1.17.0 typing-extensions-4.7.1 urllib3-1.26.20 wrapt-1.16.0 zipp-3.15.0
sh-4.2$ export PATH=$PATH:/home/ssm-user/.local/bin
sh-4.2$ 
````

## Task 3: Encrypt and Decrypt Data

In this task, I created sample text files containing mock sensitive data. I started by generating three files and adding content to one of them (`secret1.txt`). 
I verified the file contents using the `cat` command.

```bash
sh-4.2$ touch secret1.txt secret2.txt secret3.txt
sh-4.2$ echo 'TOP SECRET 1!!!' > secret1.txt
sh-4.2$ cat secret1.txt
TOP SECRET 1!!!
```

Next, I created an output directory to store encrypted files and defined a variable containing the KMS key ARN. Using the AWS Encryption CLI, I encrypted the file 
by specifying the input file, KMS key, encryption context, and output location.

```bash
sh-4.2$ mkdir output
sh-4.2$ keyArn=(arn:aws:kms:us-west-2:450871918797:key/882db9db-9f7d-4a92-b676-10a13cb4f7ea)
```

While attempting to run the encryption command, I encountered a `ModuleNotFoundError` related to `importlib.metadata`. This issue occurred because 
the EC2 instance in the lab environment uses Python 3.7, which does not natively support the `importlib.metadata` module required by newer 
versions of the AWS Encryption CLI.

Although the `importlib-metadata` package was already installed, the CLI version in use expected a newer Python environment (Python 3.8 or later).
To resolve this compatibility issue, I uninstalled the current version of the AWS Encryption CLI and installed an older version that supports Python 3.7.

```bash
pip3 uninstall aws-encryption-sdk-cli -y
pip3 install "aws-encryption-sdk-cli<4.0"
```

After downgrading the CLI, the encryption command executed successfully, allowing me to proceed with encrypting and decrypting the files as required.

```bash
sh-4.2$ aws-encryption-cli --encrypt \
>                      --input secret1.txt \
>                      --wrapping-keys key=$keyArn \
>                      --metadata-output ~/metadata \
>                      --encryption-context purpose=test \
>                      --commitment-policy require-encrypt-require-decrypt \
>                      --output ~/output/.
/home/ssm-user/.local/lib/python3.7/site-packages/aws_encryption_sdk/internal/crypto/elliptic_curve.py:21: CryptographyDeprecationWarning: int_from_bytes is deprecated, use int.from_bytes instead
  from cryptography.utils import int_from_bytes, int_to_bytes
sh-4.2$
```

After running the encryption command, I confirmed its success by checking the exit status and listing the output directory. 
The encrypted file (`secret1.txt.encrypted`) contained unreadable ciphertext, demonstrating that the encryption process was successful.

```bash
sh-4.2$ echo $?
0
sh-4.2$ ls output
secret1.txt.encrypted
sh-4.2$ cd output
sh-4.2$ cat secret1.txt.encrypted
x�΄�Z�t�Z��J�"v5�B������+��
                           o�naws-crypto-public-keyDA7rAT6h7lvSCYrEJvJZH/+6LrzwdM74eDRW54P+87A6khtr4bD6cHIFhAJT77inEfA==purposetestaws-kmsKarn:aws:kms:us-west-2:450871918797:key/882db9db-9f7d-4a92-b676-10a13cb4f7ea�x��Н(�h  ����Gs9O�g��I�*����(G�&�n�?�
                                                                                                                                                                                                                                                           �0o0m0h~0`�He.0  *�H��
              �
sh-4.2$
```

I then decrypted the file using the corresponding CLI command and verified that the output file (`secret1.txt.encrypted.decrypted`) contained the original plaintext content.

This process demonstrated how symmetric encryption uses the same key for both encryption and decryption, ensuring data confidentiality.

```bash
sh-4.2$ aws-encryption-cli --decrypt \
>                      --input secret1.txt.encrypted \
>                      --wrapping-keys key=$keyArn \
>                      --commitment-policy require-encrypt-require-decrypt \
>                      --encryption-context purpose=test \
>                      --metadata-output ~/metadata \
>                      --max-encrypted-data-keys 1 \
>                      --buffer \
>                      --output .
/home/ssm-user/.local/lib/python3.7/site-packages/aws_encryption_sdk/internal/crypto/elliptic_curve.py:21: CryptographyDeprecationWarning: int_from_bytes is deprecated, use int.from_bytes instead
  from cryptography.utils import int_from_bytes, int_to_bytes
sh-4.2$ ls
secret1.txt.encrypted  secret1.txt.encrypted.decrypted
sh-4.2$ cat secret1.txt.encrypted.decrypted
TOP SECRET 1!!!
sh-4.2$
```


## Conclusion
In this lab, I successfully implemented data protection using encryption within AWS. I created a KMS key, configured an EC2 instance to use secure credentials, and installed the AWS Encryption CLI. I then encrypted plaintext data into ciphertext and decrypted it back into its original form.

This lab demonstrated the practical use of encryption for securing sensitive data and highlighted the importance of key management in maintaining data security.

In summary:
- I created an AWS KMS encryption key
- I installed the AWS Encryption CLI
_ I encrypted plaintext
- I decrypted ciphertext


## AWS CLI Commands

```bash
# Configures AWS CLI with credentials and default region
aws configure

# Encrypts the plaintext file using the specified AWS KMS key
aws-encryption-cli --encrypt \
  --input secret1.txt \
  --wrapping-keys key=$keyArn \
  --metadata-output ~/metadata \
  --encryption-context purpose=test \
  --commitment-policy require-encrypt-require-decrypt \
  --output ~/output/.

# Checks the exit status of the previous command (0 indicates success)
echo $?

# Decrypts the encrypted file back into plaintext using the same KMS key
aws-encryption-cli --decrypt \
  --input secret1.txt.encrypted \
  --wrapping-keys key=$keyArn \
  --commitment-policy require-encrypt-require-decrypt \
  --encryption-context purpose=test \
  --metadata-output ~/metadata \
  --max-encrypted-data-keys 1 \
  --buffer \
  --output .
```
