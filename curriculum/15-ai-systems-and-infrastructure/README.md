# 15 — AI Systems & Infrastructure

This track studies the engineering systems required to train, serve, scale, observe, and operate modern AI workloads.

## Compute fundamentals
- CPUs, GPUs, TPUs, and accelerators
- memory hierarchy
- compute versus memory bottlenecks
- tensor operations and kernels
- throughput versus latency

## Training systems
- data loading pipelines
- distributed data parallelism
- model parallelism
- tensor and pipeline parallelism
- sharding concepts
- mixed precision
- checkpointing
- fault tolerance
- cluster scheduling concepts
- reproducible distributed training

## Inference systems
- batching
- dynamic batching
- caching
- KV-cache fundamentals
- model quantization
- model compression
- speculative decoding concepts
- routing
- autoscaling
- latency and throughput optimization
- cost/performance analysis

## Serving architecture
- online and batch inference
- synchronous and asynchronous serving
- APIs and gateways
- queues
- streaming responses
- model gateways
- rate limiting
- multi-model serving

## Retrieval infrastructure
- embedding pipelines
- vector indexes
- approximate nearest-neighbor search
- hybrid retrieval infrastructure
- reranking services
- index freshness and updates

## Observability
- logs, metrics, and traces
- model telemetry
- prompt and response tracing
- latency and cost monitoring
- quality monitoring
- drift monitoring
- incident debugging

## Platform engineering
- experiment platforms
- model registries
- feature stores
- data/version lineage
- orchestration
- CI/CD for ML and AI
- evaluation pipelines
- governance hooks
- multi-tenant AI platforms

## Production design
- reliability and availability
- fallbacks
- graceful degradation
- capacity planning
- cost controls
- privacy-aware architecture
- human approval paths
- release strategies

This track complements `10-ml-engineering`: that track teaches the ML lifecycle, while this track goes deeper into the systems architecture behind large-scale AI workloads.
