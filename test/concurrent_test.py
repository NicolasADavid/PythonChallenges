import concurrent.futures
# import urllib.request
import random 
import datetime
import time
import uuid

import asyncio

def do_something_1():
     
    def helper(id, seconds, name):
        print(f"ProcID: {id} \t ProcName {name} \t Sleeping {seconds} \t at {str(datetime.datetime.now())[:19][11:]}")
        time.sleep(seconds)

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        for i in range(20):
            executor.submit(helper
                , id = i
                , seconds = random.randint(1,6)
                , name = str(uuid.uuid4())[:6].upper())
            
    print(f"Finished at {str(datetime.datetime.now())[:19][11:]}")

def do_something_2():
    async def set_after(fut, delay, value):
        # Sleep for *delay* seconds.
        await asyncio.sleep(delay)

        # Set *value* as a result of *fut* Future.
        fut.set_result(value)

    async def main():
        # Get the current event loop.
        loop = asyncio.get_running_loop()

        # Create a new Future object.
        fut = loop.create_future()

        # Run "set_after()" coroutine in a parallel Task.
        # We are using the low-level "loop.create_task()" API here because
        # we already have a reference to the event loop at hand.
        # Otherwise we could have just used "asyncio.create_task()".
        loop.create_task(
            set_after(fut, 1, '... world'))

        print('hello ...')

        # Wait until *fut* has a result (1 second) and print it.
        print(await fut)

    asyncio.run(main())

def process_item(item):
    # Simulate some work
    time.sleep(1)
    return f"Processed {item}"

def main():
    items = ["item1", "item2", "item3", "item4", "item5"]
    
    # Using ThreadPoolExecutor (good for I/O-bound tasks)
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        # Submit all tasks and collect future objects
        future_to_item = {executor.submit(process_item, item): item for item in items}
        
        # Process results as they complete
        for future in concurrent.futures.as_completed(future_to_item):
            item = future_to_item[future]
            try:
                data = future.result()
                print(f"Result: {data}")
            except Exception as exc:
                print(f"{item} generated an exception: {exc}")
    
    # Alternative simpler approach using map
    print("\nUsing map:")
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        # ProcessPoolExecutor is better for CPU-bound tasks
        results = executor.map(process_item, items)
        for result in results:
            print(f"Result: {result}")

if __name__ == "__main__":
    start = time.time()
    main()
    print(f"Total execution time: {time.time() - start:.2f} seconds")