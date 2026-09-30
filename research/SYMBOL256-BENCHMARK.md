# Symbol256 Benchmark Methodology

The current Symbol256 mechanism should be evaluated as a fixed-width semantic feature representation, not presumed lossless compression.

Measurements: source bytes; symbolic bytes; empirical digit entropy; unique representations; collision groups; paraphrase stability; negation sensitivity; retrieval/task retention; and exact reconstruction status.

A lossless-compression claim requires an encoder/decoder pair and byte-for-byte reconstruction. The current semantic encoder intentionally discards source detail, so exact reconstruction is not demonstrated.

The next experimental stage should compare Symbol256 against SHA-256 fingerprints, TF-IDF, embeddings, and conventional lossless compressors using identical corpora and report storage cost, collisions, retrieval precision/recall, entropy, mutual information, latency, and reconstruction.
