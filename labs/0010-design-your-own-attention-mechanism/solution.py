import numpy as np

def attention(Q, K, V):
    """
    Compute attention over a sequence.
    
    Args:
        Q: Query matrix, shape (batch_size, query_len, dim)
        K: Key matrix, shape (batch_size, key_len, dim)
        V: Value matrix, shape (batch_size, key_len, dim)
    
    Returns:
        output: Attended values, shape (batch_size, query_len, dim)
    
    The attention mechanism should:
    1. Compute compatibility between queries and keys
    2. Convert to attention weights (non-negative, sum to 1)
    3. Use weights to compute weighted sum of values
    """
    batch_size, query_len, dim = Q.shape
    _, key_len, _ = K.shape
    
    # Your implementation here
    # Hint: Think about how queries "ask questions" and keys "provide answers"
    
    A = Q @ np.transpose(K, (0,2,1))
    scaled_A = (key_len**-0.5) * A
    softmax_A = np.exp(A)/(np.sum(np.exp(A - np.max(A, axis=2, keepdims=True)), axis=2, keepdims=True))
    return softmax_A @ V

