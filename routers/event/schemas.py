from pydantic import BaseModel


class EventBase(BaseModel):
    name: str
    description: str


class EventCreate(EventBase):
    pass


class Event(EventBase):
    id: int
    image_path: str  # This will store the path to the image

    class Config:
        orm_mode = True


# Define a function to generate the path for saving images
def generate_image_path(filename):
    return f"media/occasions/{filename}"
