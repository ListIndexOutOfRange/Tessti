from yass import schedule


schedule(
    name='example',
    working_dir='.',
    jobs_dir='jobs',
    partition='publicgpu',
    account='miv',
    node=1,
    task=1,
    cpu=1,
    gpu=1,
    ram=16,
    constraint='gpua100|gpurtx6000|gpurtx5000|gpuv100',
    modules=['python/Anaconda3-2019', 'cuda/cuda-11.6', 'gcc/gcc-11'],
    commands=[
        'source /usr/local/Anaconda/Anaconda3-2019.07/etc/profile.d/conda.sh',
        'conda deactivate',
        'conda activate torch2cu118',
    ],
    file='script',
    function='add',
    args=dict(a=1, b=2),
    schedule=dict(a=[1, 2, 3], b=[4, 5, 6])
)
