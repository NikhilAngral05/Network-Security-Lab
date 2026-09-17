Experiment 2: SHA-256 Hash Generation and Data Integrity Verification
Aim

To generate a SHA-256 hash of a file and verify its integrity by comparing the generated hash values.

Methodology

The experiment uses the SHA-256 hashing algorithm to create a unique fixed-length hash for a file. The initial hash is stored separately and later compared with the newly generated hash to detect any changes.

Procedure
Create sample.txt by taking content from the user.
Generate the SHA-256 hash of the original file.
Store the original hash in original_hash.txt.
Modify the file if needed.
Generate the hash of the modified/current file.
Compare the two hash values to check the file integrity.
Result

The SHA-256 hash was generated successfully, and any changes made to the file were detected by comparing the original and current hash values.

Discussion

A small change in the file content results in a completely different SHA-256 hash. Therefore, SHA-256 can be used to check whether a file has been altered.

Improvement

The original hash is stored in a separate file, allowing the file integrity to be checked again whenever required.

Conclusion

The experiment successfully demonstrated how SHA-256 hashing can be used to generate hash values and verify the integrity of a file.
