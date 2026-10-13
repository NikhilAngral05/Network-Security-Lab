# Experiment 2: Generate SHA-256 Hash and Verify Data Integrity

## Aim

To generate a SHA-256 hash and verify the integrity of a file by comparing its hash values.

## Methodology

The experiment uses the SHA-256 hashing algorithm to generate a fixed-length hash for the file. The original hash is stored separately and compared with the current hash to identify any modification.

## Procedure

1. Create `sample.txt` using the content entered by the user.
2. Generate the SHA-256 hash of the original file.
3. Save the original hash in `original_hash.txt`.
4. Modify the file if required.
5. Generate the current hash.
6. Compare both hashes to verify file integrity.


## Result

The SHA-256 hash was successfully generated and file modifications were detected by comparing the hash values.

## Discussion

Even a small change in file content produces a different SHA-256 hash, making it useful for data integrity verification.

## Improvement

The original hash is saved separately for future integrity verification.

## Conclusion

The experiment successfully demonstrated file integrity verification using SHA-256 hashing.
