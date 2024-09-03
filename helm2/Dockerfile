FROM python:3.8-bullseye
WORKDIR /code
COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN echo 'entries: [{description: "mmlu:subject=philosophy,model=openai/gpt2", priority: 1}]' > run_entries.conf
RUN helm-run --conf-paths run_entries.conf --suite v1 --max-eval-instances 10
RUN helm-summarize --suite v1 
CMD ["helm-server", "--p", "8888"]